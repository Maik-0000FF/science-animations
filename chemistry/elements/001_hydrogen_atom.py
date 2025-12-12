#!/usr/bin/env python3
"""
Das Wasserstoffatom / The Hydrogen Atom
Bohr-Atommodell mit Periodensystem / Bohr atomic model with periodic table

Verwendung / Usage:
    manim -qk --fps 60 001_hydrogen_atom.py HydrogenAtomDE
    manim -qk --fps 60 001_hydrogen_atom.py HydrogenAtomEN
"""

from manim import *
import numpy as np

# =============================================================================
# FARBEN / COLORS
# =============================================================================
COLORS = {
    "proton": "#FF6B6B",           # Rot fuer Protonen / Red for protons
    "element_bg": "#2C2C2C",       # Element-Hintergrund / Element background
    "element_highlight": "#FFD43B", # Hervorgehobenes Element / Highlighted element
}

# Elektronenhuellen-Farben (K, L, M, N, O, P, Q) / Electron shell colors
# Innere Schalen kuehle Farben, aeussere warme / Inner shells cool, outer warm
SHELL_COLORS = {
    "K": "#BE4BDB",  # Violett / Purple - 1. Schale (innerste)
    "L": "#228BE6",  # Blau / Blue - 2. Schale
    "M": "#22B8CF",  # Cyan - 3. Schale
    "N": "#51CF66",  # Gruen / Green - 4. Schale
    "O": "#FFD43B",  # Gelb / Yellow - 5. Schale
    "P": "#FF922B",  # Orange - 6. Schale
    "Q": "#FF6B6B",  # Rot / Red - 7. Schale (aeusserste)
}

SHELL_NAMES = ["K", "L", "M", "N", "O", "P", "Q"]

# Elementgruppen-Farben / Element group colors
ELEMENT_COLORS = {
    "alkali": "#FF6B6B",        # Alkalimetalle / Alkali metals
    "alkaline": "#FFB347",      # Erdalkalimetalle / Alkaline earth metals
    "transition": "#4ECDC4",    # Uebergangsmetalle / Transition metals
    "post_transition": "#45B7D1", # Metalle / Post-transition metals
    "metalloid": "#96CEB4",     # Halbmetalle / Metalloids
    "nonmetal": "#FFEAA7",      # Nichtmetalle / Nonmetals
    "halogen": "#DDA0DD",       # Halogene / Halogens
    "noble": "#87CEEB",         # Edelgase / Noble gases
    "lanthanide": "#F0E68C",    # Lanthanoide / Lanthanides
    "actinide": "#FFB6C1",      # Actinoide / Actinides
}

# =============================================================================
# TEXTE / TEXTS
# =============================================================================
TEXT_DE = {
    "hydrogen_atom": "Das Wasserstoffatom",
    "periodic_table": "Periodensystem der Elemente",
    "nucleus": "Atomkern",
    "electron_shell": "Schale",
    "atomic_number": "Ordnungszahl",
    "mass_number": "Massenzahl",
    "latin_name": "Lateinisch",
}

TEXT_EN = {
    "hydrogen_atom": "The Hydrogen Atom",
    "periodic_table": "Periodic Table of Elements",
    "nucleus": "Nucleus",
    "electron_shell": "Shell",
    "atomic_number": "Atomic Number",
    "mass_number": "Mass Number",
    "latin_name": "Latin",
}

# =============================================================================
# PERIODENSYSTEM / PERIODIC TABLE
# =============================================================================
# Format: (Spalte, Zeile): (Symbol, Ordnungszahl, Gruppe)
PERIODIC_TABLE = {
    # Periode 1
    (0, 0): ("H", 1, "nonmetal"),
    (17, 0): ("He", 2, "noble"),
    # Periode 2
    (0, 1): ("Li", 3, "alkali"),
    (1, 1): ("Be", 4, "alkaline"),
    (12, 1): ("B", 5, "metalloid"),
    (13, 1): ("C", 6, "nonmetal"),
    (14, 1): ("N", 7, "nonmetal"),
    (15, 1): ("O", 8, "nonmetal"),
    (16, 1): ("F", 9, "halogen"),
    (17, 1): ("Ne", 10, "noble"),
    # Periode 3
    (0, 2): ("Na", 11, "alkali"),
    (1, 2): ("Mg", 12, "alkaline"),
    (12, 2): ("Al", 13, "post_transition"),
    (13, 2): ("Si", 14, "metalloid"),
    (14, 2): ("P", 15, "nonmetal"),
    (15, 2): ("S", 16, "nonmetal"),
    (16, 2): ("Cl", 17, "halogen"),
    (17, 2): ("Ar", 18, "noble"),
    # Periode 4
    (0, 3): ("K", 19, "alkali"),
    (1, 3): ("Ca", 20, "alkaline"),
    (2, 3): ("Sc", 21, "transition"),
    (3, 3): ("Ti", 22, "transition"),
    (4, 3): ("V", 23, "transition"),
    (5, 3): ("Cr", 24, "transition"),
    (6, 3): ("Mn", 25, "transition"),
    (7, 3): ("Fe", 26, "transition"),
    (8, 3): ("Co", 27, "transition"),
    (9, 3): ("Ni", 28, "transition"),
    (10, 3): ("Cu", 29, "transition"),
    (11, 3): ("Zn", 30, "transition"),
    (12, 3): ("Ga", 31, "post_transition"),
    (13, 3): ("Ge", 32, "metalloid"),
    (14, 3): ("As", 33, "metalloid"),
    (15, 3): ("Se", 34, "nonmetal"),
    (16, 3): ("Br", 35, "halogen"),
    (17, 3): ("Kr", 36, "noble"),
    # Periode 5
    (0, 4): ("Rb", 37, "alkali"),
    (1, 4): ("Sr", 38, "alkaline"),
    (2, 4): ("Y", 39, "transition"),
    (3, 4): ("Zr", 40, "transition"),
    (4, 4): ("Nb", 41, "transition"),
    (5, 4): ("Mo", 42, "transition"),
    (6, 4): ("Tc", 43, "transition"),
    (7, 4): ("Ru", 44, "transition"),
    (8, 4): ("Rh", 45, "transition"),
    (9, 4): ("Pd", 46, "transition"),
    (10, 4): ("Ag", 47, "transition"),
    (11, 4): ("Cd", 48, "transition"),
    (12, 4): ("In", 49, "post_transition"),
    (13, 4): ("Sn", 50, "post_transition"),
    (14, 4): ("Sb", 51, "metalloid"),
    (15, 4): ("Te", 52, "metalloid"),
    (16, 4): ("I", 53, "halogen"),
    (17, 4): ("Xe", 54, "noble"),
    # Periode 6
    (0, 5): ("Cs", 55, "alkali"),
    (1, 5): ("Ba", 56, "alkaline"),
    (2, 5): ("La", 57, "lanthanide"),
    (3, 5): ("Hf", 72, "transition"),
    (4, 5): ("Ta", 73, "transition"),
    (5, 5): ("W", 74, "transition"),
    (6, 5): ("Re", 75, "transition"),
    (7, 5): ("Os", 76, "transition"),
    (8, 5): ("Ir", 77, "transition"),
    (9, 5): ("Pt", 78, "transition"),
    (10, 5): ("Au", 79, "transition"),
    (11, 5): ("Hg", 80, "transition"),
    (12, 5): ("Tl", 81, "post_transition"),
    (13, 5): ("Pb", 82, "post_transition"),
    (14, 5): ("Bi", 83, "post_transition"),
    (15, 5): ("Po", 84, "metalloid"),
    (16, 5): ("At", 85, "halogen"),
    (17, 5): ("Rn", 86, "noble"),
    # Periode 7
    (0, 6): ("Fr", 87, "alkali"),
    (1, 6): ("Ra", 88, "alkaline"),
    (2, 6): ("Ac", 89, "actinide"),
    (3, 6): ("Rf", 104, "transition"),
    (4, 6): ("Db", 105, "transition"),
    (5, 6): ("Sg", 106, "transition"),
    (6, 6): ("Bh", 107, "transition"),
    (7, 6): ("Hs", 108, "transition"),
    (8, 6): ("Mt", 109, "transition"),
    (9, 6): ("Ds", 110, "transition"),
    (10, 6): ("Rg", 111, "transition"),
    (11, 6): ("Cn", 112, "transition"),
    (12, 6): ("Nh", 113, "post_transition"),
    (13, 6): ("Fl", 114, "post_transition"),
    (14, 6): ("Mc", 115, "post_transition"),
    (15, 6): ("Lv", 116, "post_transition"),
    (16, 6): ("Ts", 117, "halogen"),
    (17, 6): ("Og", 118, "noble"),
    # Lanthanoide (Reihe 8)
    (3, 8): ("Ce", 58, "lanthanide"),
    (4, 8): ("Pr", 59, "lanthanide"),
    (5, 8): ("Nd", 60, "lanthanide"),
    (6, 8): ("Pm", 61, "lanthanide"),
    (7, 8): ("Sm", 62, "lanthanide"),
    (8, 8): ("Eu", 63, "lanthanide"),
    (9, 8): ("Gd", 64, "lanthanide"),
    (10, 8): ("Tb", 65, "lanthanide"),
    (11, 8): ("Dy", 66, "lanthanide"),
    (12, 8): ("Ho", 67, "lanthanide"),
    (13, 8): ("Er", 68, "lanthanide"),
    (14, 8): ("Tm", 69, "lanthanide"),
    (15, 8): ("Yb", 70, "lanthanide"),
    (16, 8): ("Lu", 71, "lanthanide"),
    # Actinoide (Reihe 9)
    (3, 9): ("Th", 90, "actinide"),
    (4, 9): ("Pa", 91, "actinide"),
    (5, 9): ("U", 92, "actinide"),
    (6, 9): ("Np", 93, "actinide"),
    (7, 9): ("Pu", 94, "actinide"),
    (8, 9): ("Am", 95, "actinide"),
    (9, 9): ("Cm", 96, "actinide"),
    (10, 9): ("Bk", 97, "actinide"),
    (11, 9): ("Cf", 98, "actinide"),
    (12, 9): ("Es", 99, "actinide"),
    (13, 9): ("Fm", 100, "actinide"),
    (14, 9): ("Md", 101, "actinide"),
    (15, 9): ("No", 102, "actinide"),
    (16, 9): ("Lr", 103, "actinide"),
}


# =============================================================================
# ANIMATION
# =============================================================================
class HydrogenAtom(Scene):
    """
    Animation des Wasserstoffatoms / Animation of the hydrogen atom
    Zeigt Periodensystem und Bohr-Atommodell / Shows periodic table and Bohr model
    """
    def __init__(self, lang="de", **kwargs):
        self.lang = lang
        self.text = TEXT_DE if lang == "de" else TEXT_EN
        super().__init__(**kwargs)

    def create_element_box(self, symbol, number, group, size=0.7):
        """Erstellt eine Elementbox / Creates an element box"""
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

        num_text = Text(str(number), font_size=7, color=WHITE)
        num_text.move_to(bg.get_corner(UL) + RIGHT * 0.12 + DOWN * 0.1)

        sym_text = Text(symbol, font_size=16, color=WHITE, weight=BOLD)
        sym_text.move_to(bg.get_center() + DOWN * 0.02)

        box.add(bg, num_text, sym_text)
        return box

    def create_periodic_table(self):
        """Erstellt das Periodensystem / Creates the periodic table"""
        table = VGroup()
        hydrogen_box = None
        cell_size = 0.7
        gap = 0.05

        for (col, row), (symbol, number, group) in PERIODIC_TABLE.items():
            box = self.create_element_box(symbol, number, group, size=cell_size)
            x = col * (cell_size + gap)
            if row >= 8:
                y = -(row + 0.5) * (cell_size + gap)
            else:
                y = -row * (cell_size + gap)
            box.move_to([x, y, 0])
            table.add(box)
            if symbol == "H":
                hydrogen_box = box

        table.move_to(ORIGIN)
        return table, hydrogen_box

    def create_hydrogen_detail_box(self):
        """Erstellt detaillierte Wasserstoff-Box / Creates detailed hydrogen box"""
        box = VGroup()

        bg = RoundedRectangle(
            width=4, height=5.5,
            corner_radius=0.2,
            fill_color=COLORS["element_bg"],
            fill_opacity=0.9,
            stroke_color=COLORS["element_highlight"],
            stroke_width=3
        )

        num_label = Text(self.text["atomic_number"] + ":", font_size=20, color=GRAY)
        num_value = Text("1", font_size=24, color=WHITE, weight=BOLD)
        num_group = VGroup(num_label, num_value).arrange(RIGHT, buff=0.2)
        num_group.move_to(bg.get_top() + DOWN * 0.5)

        symbol = Text("H", font_size=100, color=COLORS["element_highlight"], weight=BOLD)
        symbol.move_to(bg.get_center() + UP * 0.4)

        name = Text("Hydrogen" if self.lang == "en" else "Wasserstoff",
                    font_size=26, color=WHITE)
        name.move_to(bg.get_center() + DOWN * 0.7)

        latin_label = Text(self.text["latin_name"] + ":", font_size=16, color=GRAY)
        latin_value = Text("Hydrogenium", font_size=18, color=WHITE, slant=ITALIC)
        latin_group = VGroup(latin_label, latin_value).arrange(RIGHT, buff=0.2)
        latin_group.move_to(bg.get_center() + DOWN * 1.2)

        mass_label = Text(self.text["mass_number"] + ":", font_size=18, color=GRAY)
        mass_value = Text("1.008 u", font_size=20, color=WHITE)
        mass_group = VGroup(mass_label, mass_value).arrange(RIGHT, buff=0.2)
        mass_group.move_to(bg.get_bottom() + UP * 0.6)

        box.add(bg, num_group, symbol, name, latin_group, mass_group)
        return box

    def create_bohr_model(self):
        """Erstellt Bohr-Atommodell / Creates Bohr atomic model"""
        model = VGroup()
        k_shell_color = SHELL_COLORS["K"]

        # Atomkern (Proton) / Nucleus (Proton)
        nucleus = VGroup()
        proton = Circle(radius=0.4, fill_color=COLORS["proton"],
                        fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        proton_label = Text("p+", font_size=24, color=WHITE, weight=BOLD)
        nucleus.add(proton, proton_label)

        nucleus_label = Text(self.text["nucleus"], font_size=18, color=COLORS["proton"])
        nucleus_label.next_to(nucleus, DOWN, buff=0.3)

        # Elektronenbahn (K-Schale) / Electron orbit (K-shell)
        orbit_radius = 2.0
        orbit = Circle(radius=orbit_radius, stroke_color=k_shell_color,
                       stroke_width=2, stroke_opacity=0.6)
        orbit_dashed = DashedVMobject(orbit, num_dashes=40)

        # Elektron / Electron
        electron = Circle(radius=0.2, fill_color=k_shell_color,
                          fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        electron_label = Text("e-", font_size=16, color=WHITE, weight=BOLD)
        electron_label.move_to(electron)
        electron_group = VGroup(electron, electron_label)
        electron_group.move_to([orbit_radius, 0, 0])

        shell_label = Text("K-" + self.text["electron_shell"], font_size=16, color=k_shell_color)
        shell_label.move_to([orbit_radius + 0.8, orbit_radius - 0.5, 0])

        model.add(orbit_dashed, nucleus, nucleus_label, electron_group, shell_label)
        return model, electron_group, orbit_radius

    def construct(self):
        # === TITEL / TITLE ===
        title = Text(self.text["hydrogen_atom"], font_size=42, color=WHITE)
        title.to_edge(UP, buff=0.5)

        # === PHASE 1: Periodensystem / Periodic table ===
        pt_title = Text(self.text["periodic_table"], font_size=32, color=WHITE)
        pt_title.to_edge(UP, buff=0.5)

        table, hydrogen_box = self.create_periodic_table()
        table.scale(0.65)
        table.move_to(ORIGIN + DOWN * 0.5)

        self.play(Write(pt_title), run_time=1)
        self.play(FadeIn(table), run_time=2)
        self.wait(1)

        # Wasserstoff hervorheben / Highlight hydrogen
        highlight_rect = SurroundingRectangle(
            hydrogen_box, color=COLORS["element_highlight"],
            stroke_width=4, buff=0.05
        )
        self.play(Create(highlight_rect), run_time=0.5)
        self.play(
            highlight_rect.animate.set_stroke(width=6),
            rate_func=there_and_back,
            run_time=0.5
        )
        self.wait(0.5)

        # === PHASE 2: Zoom auf Wasserstoff / Zoom to hydrogen ===
        other_elements = VGroup(*[elem for elem in table if elem != hydrogen_box])

        self.play(
            FadeOut(other_elements),
            FadeOut(highlight_rect),
            FadeOut(pt_title),
            run_time=1
        )

        detail_box = self.create_hydrogen_detail_box()
        detail_box.move_to(LEFT * 4)

        self.play(
            ReplacementTransform(hydrogen_box, detail_box),
            run_time=1.5
        )
        self.wait(0.5)

        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)

        # === PHASE 3: Atommodell / Atomic model ===
        model, electron_group, orbit_radius = self.create_bohr_model()
        model.move_to(RIGHT * 2.5)
        model.scale(1.2)

        arrow = Arrow(
            detail_box.get_right() + RIGHT * 0.2,
            model.get_left() + LEFT * 0.5,
            color=COLORS["element_highlight"],
            stroke_width=3
        )

        self.play(GrowArrow(arrow), run_time=0.5)

        orbit_dashed = model[0]
        nucleus = model[1]
        nucleus_label = model[2]
        electron_grp = model[3]
        shell_label = model[4]

        self.play(FadeIn(nucleus), run_time=1)
        self.play(Write(nucleus_label), run_time=0.5)
        self.wait(0.3)

        self.play(Create(orbit_dashed), run_time=1)
        self.play(Write(shell_label), run_time=0.5)

        self.play(FadeIn(electron_grp), run_time=0.5)
        self.wait(0.5)

        # === PHASE 4: Elektronen-Animation / Electron animation ===
        center = nucleus.get_center()

        def electron_orbit(mob, dt):
            mob.rotate(dt * 2, about_point=center)

        electron_grp.add_updater(electron_orbit)
        self.wait(4)
        electron_grp.remove_updater(electron_orbit)

        self.wait(1)

        # === ENDE / END ===
        self.play(
            FadeOut(VGroup(title, detail_box, arrow, model)),
            run_time=1.5
        )
        self.wait(0.5)


class HydrogenAtomDE(HydrogenAtom):
    """Deutsche Version / German version"""
    def __init__(self, **kwargs):
        super().__init__(lang="de", **kwargs)


class HydrogenAtomEN(HydrogenAtom):
    """English version / Englische Version"""
    def __init__(self, **kwargs):
        super().__init__(lang="en", **kwargs)
