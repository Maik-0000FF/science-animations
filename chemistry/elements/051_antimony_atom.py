"""
Das Antimonatom - YouTube Version (16:9, 4K)
The Antimony Atom

Animation zeigt:
1. Vollstaendiges Periodensystem der Elemente
2. Zoom auf Antimon-Feld
3. Vereinfachtes Bohr-Atommodell mit 5 Schale(n)
"""

from manim import *
import numpy as np

# =============================================================================
# KONSTANTEN / CONSTANTS (inline fuer Standalone)
# =============================================================================

# Farben / Colors
COLORS = {
    "proton": "#FF6B6B",   # Rot fuer Protonen / Red for protons
    "neutron": "#868E96",  # Grau fuer Neutronen / Gray for neutrons
    "electron": "#228BE6", # Blau fuer Elektronen / Blue for electrons
    "orbit": "#495057",    # Elektronenbahn / Electron orbit
    "nucleus": "#FF8787",  # Atomkern / Nucleus
}

# Elektronenhuellen-Farben / Electron shell colors
SHELL_COLORS = {
    "K": "#BE4BDB",  # Violett / Purple - 1. Schale
    "L": "#228BE6",  # Blau / Blue - 2. Schale
    "M": "#22B8CF",  # Cyan - 3. Schale
    "N": "#51CF66",  # Gruen / Green - 4. Schale
    "O": "#FFD43B",  # Gelb / Yellow - 5. Schale
    "P": "#FF922B",  # Orange - 6. Schale
    "Q": "#FF6B6B",  # Rot / Red - 7. Schale
}

SHELL_NAMES = ["K", "L", "M", "N", "O", "P", "Q"]

# Elementgruppen-Farben / Element group colors
ELEMENT_COLORS = {
    "alkali": "#FF6B6B",
    "alkaline": "#FFB347",
    "transition": "#4ECDC4",
    "post_transition": "#45B7D1",
    "metalloid": "#96CEB4",
    "nonmetal": "#FFEAA7",
    "halogen": "#DDA0DD",
    "noble": "#87CEEB",
    "lanthanide": "#F0E68C",
    "actinide": "#FFB6C1",
}

# Periodensystem / Periodic Table
PERIODIC_TABLE = {
    (0, 0): ("H", 1, "nonmetal"), (17, 0): ("He", 2, "noble"),
    (0, 1): ("Li", 3, "alkali"), (1, 1): ("Be", 4, "alkaline"),
    (12, 1): ("B", 5, "metalloid"), (13, 1): ("C", 6, "nonmetal"),
    (14, 1): ("N", 7, "nonmetal"), (15, 1): ("O", 8, "nonmetal"),
    (16, 1): ("F", 9, "halogen"), (17, 1): ("Ne", 10, "noble"),
    (0, 2): ("Na", 11, "alkali"), (1, 2): ("Mg", 12, "alkaline"),
    (12, 2): ("Al", 13, "post_transition"), (13, 2): ("Si", 14, "metalloid"),
    (14, 2): ("P", 15, "nonmetal"), (15, 2): ("S", 16, "nonmetal"),
    (16, 2): ("Cl", 17, "halogen"), (17, 2): ("Ar", 18, "noble"),
    (0, 3): ("K", 19, "alkali"), (1, 3): ("Ca", 20, "alkaline"),
    (2, 3): ("Sc", 21, "transition"), (3, 3): ("Ti", 22, "transition"),
    (4, 3): ("V", 23, "transition"), (5, 3): ("Cr", 24, "transition"),
    (6, 3): ("Mn", 25, "transition"), (7, 3): ("Fe", 26, "transition"),
    (8, 3): ("Co", 27, "transition"), (9, 3): ("Ni", 28, "transition"),
    (10, 3): ("Cu", 29, "transition"), (11, 3): ("Zn", 30, "transition"),
    (12, 3): ("Ga", 31, "post_transition"), (13, 3): ("Ge", 32, "metalloid"),
    (14, 3): ("As", 33, "metalloid"), (15, 3): ("Se", 34, "nonmetal"),
    (16, 3): ("Br", 35, "halogen"), (17, 3): ("Kr", 36, "noble"),
    (0, 4): ("Rb", 37, "alkali"), (1, 4): ("Sr", 38, "alkaline"),
    (2, 4): ("Y", 39, "transition"), (3, 4): ("Zr", 40, "transition"),
    (4, 4): ("Nb", 41, "transition"), (5, 4): ("Mo", 42, "transition"),
    (6, 4): ("Tc", 43, "transition"), (7, 4): ("Ru", 44, "transition"),
    (8, 4): ("Rh", 45, "transition"), (9, 4): ("Pd", 46, "transition"),
    (10, 4): ("Ag", 47, "transition"), (11, 4): ("Cd", 48, "transition"),
    (12, 4): ("In", 49, "post_transition"), (13, 4): ("Sn", 50, "post_transition"),
    (14, 4): ("Sb", 51, "metalloid"), (15, 4): ("Te", 52, "metalloid"),
    (16, 4): ("I", 53, "halogen"), (17, 4): ("Xe", 54, "noble"),
    (0, 5): ("Cs", 55, "alkali"), (1, 5): ("Ba", 56, "alkaline"),
    (2, 5): ("La", 57, "lanthanide"), (3, 5): ("Hf", 72, "transition"),
    (4, 5): ("Ta", 73, "transition"), (5, 5): ("W", 74, "transition"),
    (6, 5): ("Re", 75, "transition"), (7, 5): ("Os", 76, "transition"),
    (8, 5): ("Ir", 77, "transition"), (9, 5): ("Pt", 78, "transition"),
    (10, 5): ("Au", 79, "transition"), (11, 5): ("Hg", 80, "transition"),
    (12, 5): ("Tl", 81, "post_transition"), (13, 5): ("Pb", 82, "post_transition"),
    (14, 5): ("Bi", 83, "post_transition"), (15, 5): ("Po", 84, "metalloid"),
    (16, 5): ("At", 85, "halogen"), (17, 5): ("Rn", 86, "noble"),
    (0, 6): ("Fr", 87, "alkali"), (1, 6): ("Ra", 88, "alkaline"),
    (2, 6): ("Ac", 89, "actinide"), (3, 6): ("Rf", 104, "transition"),
    (4, 6): ("Db", 105, "transition"), (5, 6): ("Sg", 106, "transition"),
    (6, 6): ("Bh", 107, "transition"), (7, 6): ("Hs", 108, "transition"),
    (8, 6): ("Mt", 109, "transition"), (9, 6): ("Ds", 110, "transition"),
    (10, 6): ("Rg", 111, "transition"), (11, 6): ("Cn", 112, "transition"),
    (12, 6): ("Nh", 113, "post_transition"), (13, 6): ("Fl", 114, "post_transition"),
    (14, 6): ("Mc", 115, "post_transition"), (15, 6): ("Lv", 116, "post_transition"),
    (16, 6): ("Ts", 117, "halogen"), (17, 6): ("Og", 118, "noble"),
    (3, 8): ("Ce", 58, "lanthanide"), (4, 8): ("Pr", 59, "lanthanide"),
    (5, 8): ("Nd", 60, "lanthanide"), (6, 8): ("Pm", 61, "lanthanide"),
    (7, 8): ("Sm", 62, "lanthanide"), (8, 8): ("Eu", 63, "lanthanide"),
    (9, 8): ("Gd", 64, "lanthanide"), (10, 8): ("Tb", 65, "lanthanide"),
    (11, 8): ("Dy", 66, "lanthanide"), (12, 8): ("Ho", 67, "lanthanide"),
    (13, 8): ("Er", 68, "lanthanide"), (14, 8): ("Tm", 69, "lanthanide"),
    (15, 8): ("Yb", 70, "lanthanide"), (16, 8): ("Lu", 71, "lanthanide"),
    (3, 9): ("Th", 90, "actinide"), (4, 9): ("Pa", 91, "actinide"),
    (5, 9): ("U", 92, "actinide"), (6, 9): ("Np", 93, "actinide"),
    (7, 9): ("Pu", 94, "actinide"), (8, 9): ("Am", 95, "actinide"),
    (9, 9): ("Cm", 96, "actinide"), (10, 9): ("Bk", 97, "actinide"),
    (11, 9): ("Cf", 98, "actinide"), (12, 9): ("Es", 99, "actinide"),
    (13, 9): ("Fm", 100, "actinide"), (14, 9): ("Md", 101, "actinide"),
    (15, 9): ("No", 102, "actinide"), (16, 9): ("Lr", 103, "actinide"),
}

# Texte / Texts
TEXT_DE = {
    "periodic_table": "Periodensystem der Elemente",
    "nucleus": "Atomkern",
    "atomic_number": "Ordnungszahl",
    "mass_number": "Massenzahl",
    "latin_name": "Lateinisch",
}

TEXT_EN = {
    "periodic_table": "Periodic Table of Elements",
    "nucleus": "Nucleus",
    "atomic_number": "Atomic Number",
    "mass_number": "Mass Number",
    "latin_name": "Latin",
}

def get_text(lang="de"):
    """Gibt die Texte in der gewaehlten Sprache zurueck / Returns texts in selected language"""
    return TEXT_DE if lang == "de" else TEXT_EN


# =============================================================================
# ELEMENT-SPEZIFISCHE DATEN
# =============================================================================

ELEMENT_SYMBOL = "Sb"
ELEMENT_NUMBER = 51
ELEMENT_NAME_DE = "Antimon"
ELEMENT_NAME_EN = "Antimony"
ELEMENT_LATIN = "Stibium"
ELEMENT_MASS = "121.76 u"
ELEMENT_GROUP = "metalloid"
ELEMENT_PROTONS = 51
ELEMENT_NEUTRONS = 70

ELECTRON_CONFIG = [2, 8, 18, 18, 5, 0, 0]


def get_active_shells():
    shells = []
    for i, count in enumerate(ELECTRON_CONFIG):
        if count > 0:
            shells.append((SHELL_NAMES[i], count, SHELL_COLORS[SHELL_NAMES[i]]))
    return shells


class AntimonyAtom(Scene):
    ELEMENT_GROUP = ELEMENT_GROUP

    def __init__(self, lang="de", **kwargs):
        self.lang = lang
        self.text = get_text(lang)
        self.element_color = ELEMENT_COLORS.get(self.ELEMENT_GROUP, WHITE)
        super().__init__(**kwargs)

    def create_element_box(self, symbol, number, group, size=0.7):
        color = ELEMENT_COLORS.get(group, WHITE)
        box = VGroup()

        bg = RoundedRectangle(
            width=size, height=size,
            corner_radius=0.03,
            fill_color=color,
            fill_opacity=0.3,
            stroke_color=color,
            stroke_width=1
        )

        sym_text = Text(symbol, font_size=16, color=WHITE, weight=BOLD)
        sym_text.move_to(bg.get_center())

        box.add(bg, sym_text)
        return box

    def create_periodic_table(self):
        table = VGroup()
        target_box = None
        cell_size = 0.7
        gap = 0.05

        for (col, row), (symbol, number, group) in PERIODIC_TABLE.items():
            box = self.create_element_box(symbol, number, group, size=cell_size)
            x = col * (cell_size + gap)
            y = -(row + 0.5) * (cell_size + gap) if row >= 8 else -row * (cell_size + gap)
            box.move_to([x, y, 0])
            table.add(box)

            if symbol == ELEMENT_SYMBOL:
                target_box = box

        table.move_to(ORIGIN)
        return table, target_box

    def create_element_detail_box(self):
        box = VGroup()

        bg = RoundedRectangle(
            width=4, height=5.5,
            corner_radius=0.2,
            fill_color=self.element_color,
            fill_opacity=0.3,
            stroke_color=self.element_color,
            stroke_width=3
        )

        num_label = Text(self.text["atomic_number"] + ":", font_size=20, color=GRAY)
        num_value = Text(str(ELEMENT_NUMBER), font_size=24, color=WHITE, weight=BOLD)
        num_group = VGroup(num_label, num_value).arrange(RIGHT, buff=0.2)
        num_group.move_to(bg.get_top() + DOWN * 0.5)

        symbol = Text(ELEMENT_SYMBOL, font_size=100, color=self.element_color, weight=BOLD)
        symbol.move_to(bg.get_center() + UP * 0.4)

        name = Text(ELEMENT_NAME_EN if self.lang == "en" else ELEMENT_NAME_DE,
                    font_size=26, color=WHITE)
        name.move_to(bg.get_center() + DOWN * 0.7)

        latin_label = Text(self.text["latin_name"] + ":", font_size=16, color=GRAY)
        latin_value = Text(ELEMENT_LATIN, font_size=18, color=WHITE, slant=ITALIC)
        latin_group = VGroup(latin_label, latin_value).arrange(RIGHT, buff=0.2)
        latin_group.move_to(bg.get_center() + DOWN * 1.2)

        mass_label = Text(self.text["mass_number"] + ":", font_size=18, color=GRAY)
        mass_value = Text(ELEMENT_MASS, font_size=20, color=WHITE)
        mass_group = VGroup(mass_label, mass_value).arrange(RIGHT, buff=0.2)
        mass_group.move_to(bg.get_bottom() + UP * 0.6)

        box.add(bg, num_group, symbol, name, latin_group, mass_group)
        return box

    def create_bohr_model(self):
        model = VGroup()
        active_shells = get_active_shells()

        NUCLEUS_RADIUS = 0.35
        ELECTRON_RADIUS = 0.08
        BASE_RADIUS = 0.5
        RADIUS_STEP = 0.375

        nucleus = Circle(
            radius=NUCLEUS_RADIUS,
            fill_color=COLORS["proton"],
            fill_opacity=0.9,
            stroke_color=WHITE,
            stroke_width=2
        )

        proton_text = Text(f"{ELEMENT_PROTONS}p+", font_size=12, color=WHITE, weight=BOLD)
        neutron_text = Text(f"{ELEMENT_NEUTRONS}n", font_size=12, color=WHITE, weight=BOLD)
        nucleus_content = VGroup(proton_text, neutron_text).arrange(DOWN, buff=0.03)
        nucleus_content.move_to(nucleus)

        nucleus_group = VGroup(nucleus, nucleus_content)

        nucleus_label = Text(self.text["nucleus"], font_size=14, color=COLORS["proton"])
        nucleus_label.next_to(nucleus_group, UP, buff=0.2)

        model.add(nucleus_group, nucleus_label)

        electron_groups = []

        for i, (shell_name, electron_count, shell_color) in enumerate(active_shells):
            orbit_radius = BASE_RADIUS + i * RADIUS_STEP

            orbit = Circle(
                radius=orbit_radius,
                stroke_color=shell_color,
                stroke_width=1.5,
                stroke_opacity=0.6
            )
            orbit_dashed = DashedVMobject(orbit, num_dashes=20 + i * 8)
            model.add(orbit_dashed)

            electrons = VGroup()

            for j in range(electron_count):
                angle = 2 * PI * j / electron_count

                electron = Circle(
                    radius=ELECTRON_RADIUS,
                    fill_color=shell_color,
                    fill_opacity=1,
                    stroke_color=WHITE,
                    stroke_width=1
                )
                electron.move_to([
                    orbit_radius * np.cos(angle),
                    orbit_radius * np.sin(angle),
                    0
                ])
                electrons.add(electron)

            electron_groups.append(electrons)
            model.add(electrons)

            shell_label = Text(
                f"{shell_name}: {electron_count}",
                font_size=10,
                color=shell_color
            )
            label_angle = -PI / 2
            shell_label.move_to([
                (orbit_radius + 0.2) * np.cos(label_angle),
                (orbit_radius + 0.2) * np.sin(label_angle),
                0
            ])
            model.add(shell_label)

        return model, electron_groups, nucleus_group

    def construct(self):
        title = Text(ELEMENT_NAME_EN if self.lang == "en" else ELEMENT_NAME_DE, font_size=42, color=WHITE)
        title.to_edge(UP, buff=0.5)

        pt_title = Text(self.text["periodic_table"], font_size=32, color=WHITE)
        pt_title.to_edge(UP, buff=0.5)

        table, target_box = self.create_periodic_table()
        table.scale(0.65)
        table.move_to(ORIGIN + DOWN * 0.5)

        self.play(Write(pt_title), run_time=1)
        self.play(FadeIn(table), run_time=2)
        self.wait(1)

        highlight_rect = SurroundingRectangle(
            target_box, color=self.element_color,
            stroke_width=4, buff=0.05
        )
        self.play(Create(highlight_rect), run_time=0.5)
        self.play(highlight_rect.animate.set_stroke(width=6),
                 rate_func=there_and_back, run_time=0.5)
        self.wait(0.5)

        other_elements = VGroup(*[elem for elem in table if elem != target_box])

        self.play(
            FadeOut(other_elements),
            FadeOut(highlight_rect),
            FadeOut(pt_title),
            run_time=1
        )

        detail_box = self.create_element_detail_box()
        detail_box.move_to(LEFT * 4)

        self.play(ReplacementTransform(target_box, detail_box), run_time=1.5)
        self.wait(0.5)

        self.play(Write(title), run_time=1)

        model, electron_groups, nucleus_group = self.create_bohr_model()
        nucleus_offset = nucleus_group.get_center()
        model.shift([2.5 - nucleus_offset[0], 0 - nucleus_offset[1], 0])

        self.play(FadeIn(model[0]), run_time=1)
        self.play(Write(model[1]), run_time=0.5)
        self.wait(0.3)

        idx = 2
        for i in range(len(get_active_shells())):
            self.play(Create(model[idx]), run_time=0.6)
            self.play(FadeIn(model[idx + 1]), Write(model[idx + 2]), run_time=0.4)
            idx += 3

        self.wait(0.5)

        center = nucleus_group.get_center()

        updaters = []
        for i, electrons in enumerate(electron_groups):
            speed = 2.0 - i * 0.3
            if speed < 0.5:
                speed = 0.5

            def make_updater(spd):
                return lambda mob, dt: mob.rotate(dt * spd, about_point=center)

            updater = make_updater(speed)
            electrons.add_updater(updater)
            updaters.append((electrons, updater))

        self.wait(4)

        for electrons, updater in updaters:
            electrons.remove_updater(updater)

        self.wait(1)

        self.play(FadeOut(VGroup(title, detail_box, model)), run_time=1.5)
        self.wait(0.5)


class AntimonyAtomDE(AntimonyAtom):
    def __init__(self, **kwargs):
        super().__init__(lang="de", **kwargs)


class AntimonyAtomEN(AntimonyAtom):
    def __init__(self, **kwargs):
        super().__init__(lang="en", **kwargs)
