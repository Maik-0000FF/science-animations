# Science Animations

Standalone scientific animations with [Manim](https://www.manim.community/). Each animation is self-contained with no external dependencies.

## Installation

```bash
pip install manim numpy
```

## Rendering

```bash
# 4K (3840x2160), 60fps
manim -qk --fps 60 <file.py> <ClassName>

# Example
manim -qk --fps 60 chemistry/elements/001_hydrogen_atom.py HydrogenAtomDE
manim -qk --fps 60 chemistry/elements/079_gold_atom.py GoldAtomEN
```

## Animations

### Chemistry - All 118 Elements

Bohr atomic models for all elements of the periodic table.

| # | Element | File | Classes |
|---|---------|------|---------|
| 1 | Hydrogen | `chemistry/elements/001_hydrogen_atom.py` | `HydrogenAtomDE`, `HydrogenAtomEN` |
| 2 | Helium | `chemistry/elements/002_helium_atom.py` | `HeliumAtomDE`, `HeliumAtomEN` |
| 3 | Lithium | `chemistry/elements/003_lithium_atom.py` | `LithiumAtomDE`, `LithiumAtomEN` |
| ... | ... | ... | ... |
| 79 | Gold | `chemistry/elements/079_gold_atom.py` | `GoldAtomDE`, `GoldAtomEN` |
| ... | ... | ... | ... |
| 118 | Oganesson | `chemistry/elements/118_oganesson_atom.py` | `OganessonAtomDE`, `OganessonAtomEN` |

**Complete list:** `chemistry/elements/001_hydrogen_atom.py` through `chemistry/elements/118_oganesson_atom.py`

### Physics

| File | Animation | Classes |
|------|-----------|---------|
| `physics/thermodynamics/heating_curve.py` | Heating Curve of Water | `HeatingCurveDE`, `HeatingCurveEN` |

## Languages

All animations are available in German (`*DE`) and English (`*EN`).

## Structure

```
science-animations/
├── physics/
│   └── thermodynamics/
│       └── heating_curve.py
└── chemistry/
    └── elements/
        ├── 001_hydrogen_atom.py
        ├── 002_helium_atom.py
        ├── ...
        └── 118_oganesson_atom.py
```

## Element Groups

| Group | Color | Elements |
|-------|-------|----------|
| Alkali Metals | #FF6B6B | Li, Na, K, Rb, Cs, Fr |
| Alkaline Earth | #FFB347 | Be, Mg, Ca, Sr, Ba, Ra |
| Transition Metals | #4ECDC4 | Sc-Zn, Y-Cd, Hf-Hg, Rf-Cn |
| Post-Transition | #45B7D1 | Al, Ga, In, Sn, Tl, Pb, Bi, Nh, Fl, Mc, Lv |
| Metalloids | #96CEB4 | B, Si, Ge, As, Sb, Te, Po |
| Nonmetals | #FFEAA7 | H, C, N, O, P, S, Se |
| Halogens | #DDA0DD | F, Cl, Br, I, At, Ts |
| Noble Gases | #87CEEB | He, Ne, Ar, Kr, Xe, Rn, Og |
| Lanthanides | #F0E68C | La-Lu (57-71) |
| Actinides | #FFB6C1 | Ac-Lr (89-103) |

## License

MIT License
