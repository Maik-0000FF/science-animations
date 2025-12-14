# Science Animations

Standalone scientific animations with [Manim](https://www.manim.community/). Each animation is self-contained with no external dependencies.

## Requirements

### System Dependencies

**ffmpeg** is required for video encoding:

```bash
# Arch Linux
sudo pacman -S ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### Python Dependencies

Python 3.8+ required.

```bash
pip install manim numpy
```

Or with virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
pip install manim numpy
```

## Example

![Hydrogen Atom Animation](examples/HydrogenAtomDE.gif)

*Hydrogen atom - Bohr model (720p, 30fps) | [Full quality MP4](examples/HydrogenAtomDE.mp4) (1080p, 60fps)*

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Maik-0000FF/science-animations.git
cd science-animations

# Render an animation (uses manim.cfg for settings)
manim render chemistry/elements/001_hydrogen_atom.py HydrogenAtomDE

# Output: media/videos/001_hydrogen_atom/1080p60/HydrogenAtomDE.mp4
```

## Configuration

The included `manim.cfg` provides default settings:

| Setting | Value | Description |
|---------|-------|-------------|
| background_color | #1a1a2e | Dark blue background |
| frame_rate | 60 | 60 fps |
| pixel_width | 3840 | 4K width |
| pixel_height | 2160 | 4K height |

### Quality Presets

```bash
# Preview (480p, fast)
manim render -ql chemistry/elements/001_hydrogen_atom.py HydrogenAtomDE

# HD (1080p)
manim render -qh chemistry/elements/001_hydrogen_atom.py HydrogenAtomDE

# 4K (uses manim.cfg settings)
manim render -qk chemistry/elements/001_hydrogen_atom.py HydrogenAtomDE
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
├── manim.cfg                 # Manim configuration (background, resolution)
├── examples/
│   ├── HydrogenAtomDE.gif    # Preview (720p, 30fps)
│   └── HydrogenAtomDE.mp4    # Full quality (1080p, 60fps)
├── chemistry/
│   └── elements/
│       ├── 001_hydrogen_atom.py
│       ├── 002_helium_atom.py
│       ├── ...
│       └── 118_oganesson_atom.py
├── physics/
│   └── thermodynamics/
│       └── heating_curve.py
└── media/                    # Output directory (generated)
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
