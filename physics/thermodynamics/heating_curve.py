"""
Heating Curve of Water / Erwaermungskurve von Wasser

Standalone Manim animation showing the temperature progression
when heating ice to steam with phase transitions
(plateaus at 0°C and 100°C).

Usage:
    manim -qh heating_curve.py HeatingCurveEN  # English 4K
    manim -qh heating_curve.py HeatingCurveDE  # German 4K

Requirements:
    - manim (pip install manim)
    - numpy

Source: https://github.com/Maik-0000FF/science-animations
License: MIT
"""

from manim import *
import numpy as np


# =============================================================================
# COLOURS / FARBEN
# =============================================================================

COLORS = {
    # General / Allgemein
    "axis": "#FFFFFF",      # Axes / Achsen
    "grid": "#495057",      # Grid / Gitter
    "highlight": "#FFD43B", # Highlight / Hervorhebung

    # Thermodynamics / Thermodynamik
    "ice": "#A5D8FF",       # Light blue for ice / Hellblau fuer Eis
    "water": "#228BE6",     # Blue for water / Blau fuer Wasser
    "steam": "#DEE2E6",     # Grey for steam / Grau fuer Dampf
    "heat": "#FF6B6B",      # Red for heat / Rot fuer Waerme
}


# =============================================================================
# TEXTS / TEXTE
# =============================================================================

TEXT_DE = {
    "heating_curve": "Erwaermungskurve von Wasser",
    "ice": "Eis",
    "water": "Wasser",
    "steam": "Wasserdampf",
    "melting": "Schmelzen",
    "boiling": "Verdampfen",
    "energy": "Energie",
    "temperature": "Temperatur",
    "unit_temp": "°C",
}

TEXT_EN = {
    "heating_curve": "Heating Curve of Water",
    "ice": "Ice",
    "water": "Water",
    "steam": "Steam",
    "melting": "Melting",
    "boiling": "Boiling",
    "energy": "Energy",
    "temperature": "Temperature",
    "unit_temp": "°C",
}


def get_text(lang="de"):
    """Returns texts in selected language / Gibt Texte in gewaehlter Sprache zurueck"""
    return TEXT_DE if lang == "de" else TEXT_EN


# =============================================================================
# LAYOUT MANAGER
# =============================================================================

class LayoutManager:
    """
    Central layout manager that tracks all placed elements
    and automatically prevents overlaps.
    """

    # Screen boundaries (16:9 Manim standard)
    FRAME_WIDTH = 14.2
    FRAME_HEIGHT = 8.0
    SCREEN_LEFT = -FRAME_WIDTH / 2
    SCREEN_RIGHT = FRAME_WIDTH / 2
    SCREEN_TOP = FRAME_HEIGHT / 2
    SCREEN_BOTTOM = -FRAME_HEIGHT / 2

    # Standard spacing
    MARGIN_TOP = 0.6
    MARGIN_SIDE = 0.8
    MARGIN_BOTTOM = 0.6

    PADDING_XS = 0.1
    PADDING_S = 0.2
    PADDING_M = 0.35
    PADDING_L = 0.5

    # Axis configuration
    AXIS_TIP_LENGTH = 0.25
    AXIS_TIP_WIDTH = 0.125

    def __init__(self):
        self.placed_objects = []
        self.zones = {}
        self.title = None

    def reset(self):
        self.placed_objects = []
        self.zones = {}
        self.title = None

    def set_title(self, title_obj):
        self.title = title_obj
        self.register(title_obj, zone="title")

    def get_content_bounds(self):
        bounds = {
            'left': self.SCREEN_LEFT + self.MARGIN_SIDE,
            'right': self.SCREEN_RIGHT - self.MARGIN_SIDE,
            'top': self.SCREEN_TOP - self.MARGIN_TOP,
            'bottom': self.SCREEN_BOTTOM + self.MARGIN_BOTTOM
        }
        if self.title is not None:
            bounds['top'] = self.title.get_bottom()[1] - self.PADDING_M
        return bounds

    def register(self, obj, zone=None):
        if obj not in self.placed_objects:
            self.placed_objects.append(obj)
        if zone:
            if zone not in self.zones:
                self.zones[zone] = []
            self.zones[zone].append(obj)

    def get_bbox_with_padding(self, obj, padding=None):
        if padding is None:
            padding = self.PADDING_S
        try:
            bbox = obj.get_bounding_box()
        except (AttributeError, ValueError):
            try:
                center = obj.get_center()
                width = obj.width if hasattr(obj, 'width') else 0.5
                height = obj.height if hasattr(obj, 'height') else 0.5
                return {
                    'left': center[0] - width/2 - padding,
                    'right': center[0] + width/2 + padding,
                    'bottom': center[1] - height/2 - padding,
                    'top': center[1] + height/2 + padding
                }
            except:
                return {
                    'left': -0.5 - padding,
                    'right': 0.5 + padding,
                    'bottom': -0.5 - padding,
                    'top': 0.5 + padding
                }
        return {
            'left': bbox[0][0] - padding,
            'right': bbox[2][0] + padding,
            'bottom': bbox[0][1] - padding,
            'top': bbox[2][1] + padding
        }

    def check_overlap(self, obj1, obj2, padding=None):
        if padding is None:
            padding = self.PADDING_XS
        b1 = self.get_bbox_with_padding(obj1, padding)
        b2 = self.get_bbox_with_padding(obj2, 0)
        h_overlap = not (b1['right'] < b2['left'] or b2['right'] < b1['left'])
        v_overlap = not (b1['top'] < b2['bottom'] or b2['top'] < b1['bottom'])
        return h_overlap and v_overlap

    def has_any_overlap(self, obj, padding=None, exclude=None):
        if exclude is None:
            exclude = []
        for placed in self.placed_objects:
            if placed in exclude or placed is obj:
                continue
            if self.check_overlap(obj, placed, padding):
                return True
        return False

    def find_free_position(self, obj, preferred_pos, directions=None,
                           step=0.15, max_distance=3.0, padding=None):
        if directions is None:
            directions = [
                UP, DOWN, LEFT, RIGHT,
                UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT
            ]
        if padding is None:
            padding = self.PADDING_S

        obj.move_to(preferred_pos)
        if not self.has_any_overlap(obj, padding) and self._is_in_bounds(obj):
            return np.array(preferred_pos)

        for distance in np.arange(step, max_distance, step):
            for direction in directions:
                test_pos = np.array(preferred_pos) + direction * distance
                obj.move_to(test_pos)
                if self._is_in_bounds(obj) and not self.has_any_overlap(obj, padding):
                    return test_pos

        obj.move_to(preferred_pos)
        return np.array(preferred_pos)

    def _is_in_bounds(self, obj):
        bbox = self.get_bbox_with_padding(obj, 0)
        bounds = self.get_content_bounds()
        return (bbox['left'] >= bounds['left'] and
                bbox['right'] <= bounds['right'] and
                bbox['bottom'] >= bounds['bottom'] and
                bbox['top'] <= bounds['top'])

    def place_relative(self, obj, anchor_obj, direction, buff=None,
                       align=None, register=True):
        if buff is None:
            buff = self.PADDING_S
        obj.next_to(anchor_obj, direction, buff=buff)
        if align is not None:
            obj.align_to(anchor_obj, align)
        if self.has_any_overlap(obj, self.PADDING_XS, exclude=[anchor_obj]):
            preferred = obj.get_center()
            if np.allclose(direction, UP) or np.allclose(direction, DOWN):
                alt_dirs = [LEFT, RIGHT, direction + LEFT, direction + RIGHT]
            else:
                alt_dirs = [UP, DOWN, direction + UP, direction + DOWN]
            pos = self.find_free_position(obj, preferred, alt_dirs)
            obj.move_to(pos)
        if register:
            self.register(obj)
        return obj.get_center()


def calc_axis_range(numbers, step=None):
    """
    Calculates optimal axis range based on desired numbers.
    The last number is NOT displayed as a tick mark to avoid overlap with the arrow.
    """
    if len(numbers) < 2:
        raise ValueError("At least 2 numbers required")
    if step is None:
        step = numbers[1] - numbers[0]
    axis_min = numbers[0]
    axis_max = numbers[-1]
    numbers_to_display = list(numbers[:-1])
    return [axis_min, axis_max, step], numbers_to_display


# =============================================================================
# HEATING CURVE SCENE
# =============================================================================

class HeatingCurve(Scene):
    def __init__(self, lang="de", **kwargs):
        self.lang = lang
        self.text = get_text(lang)
        super().__init__(**kwargs)

    def construct(self):
        # Initialise layout manager
        lm = LayoutManager()

        # Title
        title = Text(self.text["heating_curve"], font_size=40, color=WHITE)
        title.to_edge(UP, buff=lm.MARGIN_TOP)
        lm.set_title(title)

        # Calculate content area
        bounds = lm.get_content_bounds()
        content_height = bounds['top'] - bounds['bottom']
        content_width = bounds['right'] - bounds['left']

        # Physical parameters (for 1 kg water)
        E1 = 41.8      # End ice heating
        E2 = 375.8     # End melting
        E3 = 793.8     # End water heating
        E4 = 3053.8    # End boiling
        E5 = 3094      # End steam heating

        # Axes - centred, slightly lower
        axes_width = content_width * 0.85
        axes_height = content_height * 0.70

        # Calculate axis ranges
        x_range, x_numbers = calc_axis_range([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])
        y_range, y_numbers = calc_axis_range([-20, 0, 20, 40, 60, 80, 100, 120, 140])

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=axes_width,
            y_length=axes_height,
            axis_config={
                "color": COLORS["axis"],
                "include_tip": True,
                "tip_length": lm.AXIS_TIP_LENGTH,
                "tip_width": lm.AXIS_TIP_WIDTH,
            },
            x_axis_config={
                "numbers_to_include": x_numbers,
                "font_size": 14,
            },
            y_axis_config={
                "numbers_to_include": y_numbers,
                "font_size": 14,
            },
        )

        # Position axes with space for labels
        axes_center_x = (bounds['left'] + bounds['right']) / 2
        axes_center_y = bounds['bottom'] + axes_height / 2 + 0.3
        axes.move_to([axes_center_x, axes_center_y, 0])
        lm.register(axes, zone="graph")

        # Axis labels with formula symbols
        x_label = Text(f"{self.text['energy']} Q (kJ)",
                      font_size=16, color=WHITE)
        lm.place_relative(x_label, axes.x_axis, DOWN, buff=lm.PADDING_S)

        y_label = Text(f"{self.text['temperature']} T ({self.text['unit_temp']})",
                      font_size=16, color=WHITE)
        y_label.rotate(90 * DEGREES)
        lm.place_relative(y_label, axes.y_axis, LEFT, buff=lm.PADDING_S)

        # Manual 0 label for Y-axis
        zero_label = MathTex("0", font_size=14, color=WHITE)
        zero_label.next_to(axes.y_axis.n2p(0), LEFT, buff=0.2)
        lm.register(zero_label)

        # Helper function for colour gradient
        def interpolate_color(color1, color2, t):
            """Interpolates between two colours (t from 0 to 1)"""
            c1 = np.array(color_to_rgb(color1))
            c2 = np.array(color_to_rgb(color2))
            return rgb_to_color(c1 + t * (c2 - c1))

        # Heating curve in segments with colour gradients
        # Segment 1: Heat ice (ice colour)
        seg1 = axes.plot(
            lambda Q: -20 + Q * (20 / E1),
            x_range=[0, E1],
            color=COLORS["ice"],
            stroke_width=4,
        )

        # Segment 2: Melting - colour gradient from ice to water
        n_gradient = 50
        seg2_parts = VGroup()
        for i in range(n_gradient):
            t_start = i / n_gradient
            t_end = (i + 1) / n_gradient
            q_start = E1 + t_start * (E2 - E1)
            q_end = E1 + t_end * (E2 - E1)
            color = interpolate_color(COLORS["ice"], COLORS["water"], t_start)
            part = axes.plot(
                lambda Q: 0,
                x_range=[q_start, q_end],
                color=color,
                stroke_width=4,
            )
            seg2_parts.add(part)
        seg2 = seg2_parts

        # Segment 3: Heat water (water colour)
        seg3 = axes.plot(
            lambda Q: (Q - E2) * (100 / (E3 - E2)),
            x_range=[E2, E3],
            color=COLORS["water"],
            stroke_width=4,
        )

        # Segment 4: Boiling - colour gradient from water to red
        seg4_parts = VGroup()
        for i in range(n_gradient):
            t_start = i / n_gradient
            t_end = (i + 1) / n_gradient
            q_start = E3 + t_start * (E4 - E3)
            q_end = E3 + t_end * (E4 - E3)
            color = interpolate_color(COLORS["water"], COLORS["heat"], t_start)
            part = axes.plot(
                lambda Q: 100,
                x_range=[q_start, q_end],
                color=color,
                stroke_width=4,
            )
            seg4_parts.add(part)
        seg4 = seg4_parts

        # Segment 5: Heat steam (red)
        seg5 = axes.plot(
            lambda Q: 100 + (Q - E4) * (20 / (E5 - E4)),
            x_range=[E4, E5],
            color=COLORS["heat"],
            stroke_width=4,
        )

        # Invisible paths for MoveAlongPath animation
        path2 = axes.plot(lambda Q: 0, x_range=[E1, E2], stroke_opacity=0)
        path4 = axes.plot(lambda Q: 100, x_range=[E3, E4], stroke_opacity=0)

        lm.register(seg1)
        lm.register(seg2)
        lm.register(seg3)
        lm.register(seg4)
        lm.register(seg5)

        # Phase labels - BELOW or BESIDE the curve
        ice_label = Text(self.text["ice"], font_size=14, color=COLORS["ice"])
        ice_pos = axes.c2p(E1/2, -20)
        ice_label.move_to(ice_pos)
        ice_label.shift(DOWN * 0.5)
        if lm.has_any_overlap(ice_label, lm.PADDING_XS):
            pos = lm.find_free_position(ice_label, ice_label.get_center(), [DOWN, LEFT, DL])
            ice_label.move_to(pos)
        lm.register(ice_label)

        water_label = Text(self.text["water"], font_size=14, color=COLORS["water"])
        water_pos = axes.c2p((E2 + E3) / 2, 50)
        water_label.move_to(water_pos)
        water_label.shift(LEFT * 0.8)
        if lm.has_any_overlap(water_label, lm.PADDING_XS):
            pos = lm.find_free_position(water_label, water_label.get_center(), [LEFT, UL, DL])
            water_label.move_to(pos)
        lm.register(water_label)

        steam_label = Text(self.text["steam"], font_size=14, color=COLORS["heat"])
        steam_pos = axes.c2p(E5, 110)
        steam_label.move_to(steam_pos)
        steam_label.shift(RIGHT * 0.3 + UP * 0.3)
        if lm.has_any_overlap(steam_label, lm.PADDING_XS):
            pos = lm.find_free_position(steam_label, steam_label.get_center(), [UR, RIGHT, UP])
            steam_label.move_to(pos)
        lm.register(steam_label)

        # Heat annotations: brace -> value -> label (from bottom to top)
        # Melting
        fusion_brace = Brace(Line(axes.c2p(E1, 0), axes.c2p(E2, 0)), UP, color=COLORS["highlight"])
        lm.register(fusion_brace)

        fusion_text = Text("334 kJ/kg", font_size=11, color=COLORS["highlight"])
        fusion_text.next_to(fusion_brace, UP, buff=lm.PADDING_XS)
        lm.register(fusion_text)

        melting_label = Text(self.text["melting"], font_size=13, color=COLORS["highlight"])
        melting_label.next_to(fusion_text, UP, buff=lm.PADDING_XS)
        lm.register(melting_label)

        # Boiling
        vapor_brace = Brace(Line(axes.c2p(E3, 100), axes.c2p(E4, 100)), UP, color=COLORS["highlight"])
        lm.register(vapor_brace)

        vapor_text = Text("2260 kJ/kg", font_size=11, color=COLORS["highlight"])
        vapor_text.next_to(vapor_brace, UP, buff=lm.PADDING_XS)
        lm.register(vapor_text)

        boiling_label = Text(self.text["boiling"], font_size=13, color=COLORS["highlight"])
        boiling_label.next_to(vapor_text, UP, buff=lm.PADDING_XS)
        lm.register(boiling_label)

        # Animated dot
        dot = Dot(color=COLORS["highlight"], radius=0.08)
        dot.move_to(axes.c2p(0, -20))

        # Animation
        self.play(Write(title), run_time=1)
        self.play(Create(axes), Write(x_label), Write(y_label), Write(zero_label), run_time=2)
        self.wait(0.5)

        # Heat ice
        self.play(FadeIn(ice_label), run_time=0.5)
        self.play(Create(seg1), run_time=1.5)

        # Melting
        self.play(FadeIn(melting_label), run_time=0.5)
        self.play(Create(seg2), run_time=2)
        self.play(
            Create(fusion_brace),
            Write(fusion_text),
            run_time=1
        )

        # Heat water
        self.play(FadeIn(water_label), run_time=0.5)
        self.play(Create(seg3), run_time=2)

        # Boiling
        self.play(FadeIn(boiling_label), run_time=0.5)
        self.play(Create(seg4), run_time=3)
        self.play(
            Create(vapor_brace),
            Write(vapor_text),
            run_time=1
        )

        # Heat steam
        self.play(FadeIn(steam_label), run_time=0.5)
        self.play(Create(seg5), run_time=1)

        self.wait(1)

        # Animated dot along the curve
        self.play(FadeIn(dot), run_time=0.3)

        self.play(MoveAlongPath(dot, seg1), run_time=1)
        self.play(MoveAlongPath(dot, path2), run_time=1.5)
        self.play(MoveAlongPath(dot, seg3), run_time=1.5)
        self.play(MoveAlongPath(dot, path4), run_time=2)
        self.play(MoveAlongPath(dot, seg5), run_time=0.5)

        self.wait(2)


class HeatingCurveDE(HeatingCurve):
    def __init__(self, **kwargs):
        super().__init__(lang="de", **kwargs)


class HeatingCurveEN(HeatingCurve):
    def __init__(self, **kwargs):
        super().__init__(lang="en", **kwargs)
