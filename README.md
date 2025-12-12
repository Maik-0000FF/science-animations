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
```

## Animations

### Physics

| File | Animation | Classes |
|------|-----------|---------|
| `physics/thermodynamics/heating_curve.py` | Heating Curve of Water | `HeatingCurveDE`, `HeatingCurveEN` |

### Chemistry

| File | Animation | Classes |
|------|-----------|---------|
| `chemistry/elements/001_hydrogen_atom.py` | Hydrogen Atom (Bohr Model) | `HydrogenAtomDE`, `HydrogenAtomEN` |
| `chemistry/elements/092_uranium_atom.py` | Uranium Atom (Bohr Model) | `UraniumAtomDE`, `UraniumAtomEN` |

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
        └── 092_uranium_atom.py
```

## License

MIT License
