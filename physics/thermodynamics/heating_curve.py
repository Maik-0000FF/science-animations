"""
Erwärmungskurve von Wasser / Heating Curve of Water
====================================================

Zeigt den Temperaturverlauf beim Erhitzen von Eis (-20°C) zu Dampf (120°C).
Shows temperature progression when heating ice (-20°C) to steam (120°C).

Die Plateaus bei 0°C und 100°C zeigen die Phasenübergänge (Schmelzen/Verdampfen).
The plateaus at 0°C and 100°C show phase transitions (melting/boiling).

Verwendung / Usage:
    manim -qk --fps 60 heating_curve.py HeatingCurveDE  # Deutsch, 4K
    manim -qk --fps 60 heating_curve.py HeatingCurveEN  # English, 4K

Anpassen / Customize:
    - COLORS: Farbschema ändern / Change color scheme
    - TEXT_DE/TEXT_EN: Beschriftungen ändern / Change labels
    - E1-E5: Energie-Werte anpassen / Adjust energy values
"""

from manim import *
import numpy as np

# =============================================================================
# FARBEN / COLORS
# =============================================================================
COLORS = {
    "ice": "#A5F2F3",       # Eis / Ice - Hellblau / Light blue
    "water": "#1E90FF",     # Wasser / Water - Blau / Blue
    "steam": "#FFB6C1",     # Dampf / Steam - Hellrot / Light red
    "heat": "#FF4500",      # Wärme / Heat - Rot-Orange / Red-orange
    "axis": "#FFFFFF",      # Achsen / Axes - Weiss / White
    "highlight": "#FFD700", # Hervorhebung / Highlight - Gold
}

# =============================================================================
# TEXTE / TEXTS
# =============================================================================
TEXT_DE = {
    "heating_curve": "Erwärmungskurve von Wasser",
    "energy": "Energie",
    "temperature": "Temperatur",
    "unit_temp": "°C",
    "ice": "Eis",
    "water": "Wasser",
    "steam": "Dampf",
    "melting": "Schmelzen",
    "boiling": "Verdampfen",
}

TEXT_EN = {
    "heating_curve": "Heating Curve of Water",
    "energy": "Energy",
    "temperature": "Temperature",
    "unit_temp": "°C",
    "ice": "Ice",
    "water": "Water",
    "steam": "Steam",
    "melting": "Melting",
    "boiling": "Boiling",
}


def get_text(lang):
    """Gibt Texte in der gewählten Sprache zurück / Returns texts in selected language"""
    return TEXT_DE if lang == "de" else TEXT_EN


# =============================================================================
# HILFSFUNKTIONEN / HELPER FUNCTIONS
# =============================================================================
def calc_axis_range(numbers, step=None):
    """
    Berechnet Achsenbereich - letzte Zahl wird nicht angezeigt (Pfeilbereich).
    Calculates axis range - last number not displayed (arrow area).

    Beispiel / Example:
        calc_axis_range([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])
        → Zeigt 0-3000, Pfeil bei 3500 / Shows 0-3000, arrow at 3500
    """
    if step is None:
        step = numbers[1] - numbers[0]
    return [numbers[0], numbers[-1], step], list(numbers[:-1])


def interpolate_color(color1, color2, t):
    """Interpoliert zwischen zwei Farben / Interpolates between two colors"""
    c1 = np.array(color_to_rgb(color1))
    c2 = np.array(color_to_rgb(color2))
    return rgb_to_color(c1 + t * (c2 - c1))


# =============================================================================
# HAUPTKLASSE / MAIN CLASS
# =============================================================================
class HeatingCurve(Scene):
    """
    Erwärmungskurve von Wasser mit Phasenübergängen.
    Heating curve of water with phase transitions.
    """

    def __init__(self, lang="de", **kwargs):
        self.lang = lang
        self.text = get_text(lang)
        super().__init__(**kwargs)

    def construct(self):
        # -----------------------------------------------------------------
        # TITEL / TITLE
        # -----------------------------------------------------------------
        title = Text(self.text["heating_curve"], font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.6)

        # -----------------------------------------------------------------
        # PHYSIKALISCHE PARAMETER (für 1 kg Wasser)
        # PHYSICAL PARAMETERS (for 1 kg water)
        # -----------------------------------------------------------------
        E1 = 41.8      # Ende Eis-Erwärmung / End ice heating
        E2 = 375.8     # Ende Schmelzen / End melting
        E3 = 793.8     # Ende Wasser-Erwärmung / End water heating
        E4 = 3053.8    # Ende Verdampfen / End boiling
        E5 = 3094      # Ende Dampf-Erwärmung / End steam heating

        # -----------------------------------------------------------------
        # ACHSEN / AXES
        # -----------------------------------------------------------------
        x_range, x_numbers = calc_axis_range([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])
        y_range, y_numbers = calc_axis_range([-20, 0, 20, 40, 60, 80, 100, 120, 140])

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=10.7,  # 85% von 12.6 (verfügbare Breite)
            y_length=4.2,   # 70% von 6.0 (verfügbare Höhe)
            axis_config={
                "color": COLORS["axis"],
                "include_tip": True,
                "tip_length": 0.25,
                "tip_width": 0.125,
            },
            x_axis_config={"numbers_to_include": x_numbers, "font_size": 14},
            y_axis_config={"numbers_to_include": y_numbers, "font_size": 14},
        )
        axes.move_to([0, -0.3, 0])

        # Achsenbeschriftungen / Axis labels
        x_label = Text(f"{self.text['energy']} Q (kJ)", font_size=16, color=WHITE)
        x_label.next_to(axes.x_axis, DOWN, buff=0.2)

        y_label = Text(f"{self.text['temperature']} T ({self.text['unit_temp']})", font_size=16, color=WHITE)
        y_label.rotate(90 * DEGREES)
        y_label.next_to(axes.y_axis, LEFT, buff=0.2)

        zero_label = MathTex("0", font_size=14, color=WHITE)
        zero_label.next_to(axes.y_axis.n2p(0), LEFT, buff=0.2)

        # -----------------------------------------------------------------
        # KURVEN-SEGMENTE / CURVE SEGMENTS
        # -----------------------------------------------------------------
        stroke_w = 4

        # Segment 1: Eis erwärmen (-20°C → 0°C) / Ice heating
        seg1 = axes.plot(
            lambda Q: -20 + Q * (20 / E1),
            x_range=[0, E1],
            color=COLORS["ice"],
            stroke_width=stroke_w,
        )

        # Segment 2: Schmelzen (0°C Plateau) / Melting plateau
        n_gradient = 50
        seg2_parts = VGroup()
        for i in range(n_gradient):
            t = i / n_gradient
            q_start = E1 + t * (E2 - E1)
            q_end = E1 + (i + 1) / n_gradient * (E2 - E1)
            color = interpolate_color(COLORS["ice"], COLORS["water"], t)
            seg2_parts.add(axes.plot(lambda Q: 0, x_range=[q_start, q_end], color=color, stroke_width=stroke_w))
        seg2 = seg2_parts

        # Segment 3: Wasser erwärmen (0°C → 100°C) / Water heating
        seg3 = axes.plot(
            lambda Q: (Q - E2) * (100 / (E3 - E2)),
            x_range=[E2, E3],
            color=COLORS["water"],
            stroke_width=stroke_w,
        )

        # Segment 4: Verdampfen (100°C Plateau) / Boiling plateau
        seg4_parts = VGroup()
        for i in range(n_gradient):
            t = i / n_gradient
            q_start = E3 + t * (E4 - E3)
            q_end = E3 + (i + 1) / n_gradient * (E4 - E3)
            color = interpolate_color(COLORS["water"], COLORS["heat"], t)
            seg4_parts.add(axes.plot(lambda Q: 100, x_range=[q_start, q_end], color=color, stroke_width=stroke_w))
        seg4 = seg4_parts

        # Segment 5: Dampf erwärmen (100°C → 120°C) / Steam heating
        seg5 = axes.plot(
            lambda Q: 100 + (Q - E4) * (20 / (E5 - E4)),
            x_range=[E4, E5],
            color=COLORS["heat"],
            stroke_width=stroke_w,
        )

        # Unsichtbare Pfade für Animation / Invisible paths for animation
        path2 = axes.plot(lambda Q: 0, x_range=[E1, E2], stroke_opacity=0)
        path4 = axes.plot(lambda Q: 100, x_range=[E3, E4], stroke_opacity=0)

        # -----------------------------------------------------------------
        # BESCHRIFTUNGEN / LABELS
        # -----------------------------------------------------------------
        ice_label = Text(self.text["ice"], font_size=14, color=COLORS["ice"])
        ice_label.move_to(axes.c2p(E1/2, -20) + DOWN * 0.5)

        water_label = Text(self.text["water"], font_size=14, color=COLORS["water"])
        water_label.move_to(axes.c2p((E2 + E3) / 2, 50) + LEFT * 0.8)

        steam_label = Text(self.text["steam"], font_size=14, color=COLORS["heat"])
        steam_label.move_to(axes.c2p(E5, 110) + RIGHT * 0.3 + UP * 0.3)

        # Wärme-Annotationen / Heat annotations
        fusion_brace = Brace(Line(axes.c2p(E1, 0), axes.c2p(E2, 0)), UP, color=COLORS["highlight"])
        fusion_text = Text("334 kJ/kg", font_size=11, color=COLORS["highlight"])
        fusion_text.next_to(fusion_brace, UP, buff=0.1)
        melting_label = Text(self.text["melting"], font_size=13, color=COLORS["highlight"])
        melting_label.next_to(fusion_text, UP, buff=0.1)

        vapor_brace = Brace(Line(axes.c2p(E3, 100), axes.c2p(E4, 100)), UP, color=COLORS["highlight"])
        vapor_text = Text("2260 kJ/kg", font_size=11, color=COLORS["highlight"])
        vapor_text.next_to(vapor_brace, UP, buff=0.1)
        boiling_label = Text(self.text["boiling"], font_size=13, color=COLORS["highlight"])
        boiling_label.next_to(vapor_text, UP, buff=0.1)

        # Animierter Punkt / Animated dot
        dot = Dot(color=COLORS["highlight"], radius=0.08)
        dot.move_to(axes.c2p(0, -20))

        # -----------------------------------------------------------------
        # ANIMATION
        # -----------------------------------------------------------------
        self.play(Write(title), run_time=1)
        self.play(Create(axes), Write(x_label), Write(y_label), Write(zero_label), run_time=2)
        self.wait(0.5)

        # Eis erwärmen / Heat ice
        self.play(FadeIn(ice_label), run_time=0.5)
        self.play(Create(seg1), run_time=1.5)

        # Schmelzen / Melting
        self.play(FadeIn(melting_label), run_time=0.5)
        self.play(Create(seg2), run_time=2)
        self.play(Create(fusion_brace), Write(fusion_text), run_time=1)

        # Wasser erwärmen / Heat water
        self.play(FadeIn(water_label), run_time=0.5)
        self.play(Create(seg3), run_time=2)

        # Verdampfen / Boiling
        self.play(FadeIn(boiling_label), run_time=0.5)
        self.play(Create(seg4), run_time=3)
        self.play(Create(vapor_brace), Write(vapor_text), run_time=1)

        # Dampf erwärmen / Heat steam
        self.play(FadeIn(steam_label), run_time=0.5)
        self.play(Create(seg5), run_time=1)

        self.wait(1)

        # Punkt-Animation / Dot animation
        self.play(FadeIn(dot), run_time=0.3)
        self.play(MoveAlongPath(dot, seg1), run_time=1)
        self.play(MoveAlongPath(dot, path2), run_time=1.5)
        self.play(MoveAlongPath(dot, seg3), run_time=1.5)
        self.play(MoveAlongPath(dot, path4), run_time=2)
        self.play(MoveAlongPath(dot, seg5), run_time=0.5)

        self.wait(2)


# =============================================================================
# SPRACHVARIANTEN / LANGUAGE VARIANTS
# =============================================================================
class HeatingCurveDE(HeatingCurve):
    """Deutsche Version / German version"""
    def __init__(self, **kwargs):
        super().__init__(lang="de", **kwargs)


class HeatingCurveEN(HeatingCurve):
    """Englische Version / English version"""
    def __init__(self, **kwargs):
        super().__init__(lang="en", **kwargs)
