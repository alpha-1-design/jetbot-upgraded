# JetNova – Cooler Open Robot Design (2026)

**JetNova** is a new open reference design that works with the entire JetBot Upgraded software stack.  
It keeps the spirit of the original JetBot (affordable, buildable, educational) but looks and feels like a modern indie robot.

> Classic JetBot chassis still works 100%.  
> JetNova is the optional “much cooler” upgrade path.

---

## Design Goals

- Looks intentional and modern (not a 2019 classroom robot)
- Highly modular – camera, LiDAR, battery, compute can be swapped
- 3D-printable on common printers (250 mm bed friendly)
- Better cable management and serviceability
- Clear mounting for pan-tilt camera + optional depth camera / LiDAR
- Aggressive but friendly aesthetic (makers want to film it)
- Still cheap enough for one person to build

---

## Key Features vs Classic JetBot

| Feature                    | Classic JetBot      | JetNova                          |
|---------------------------|---------------------|----------------------------------|
| Aesthetic                 | Boxy educational    | Sculpted, modern, “product-like” |
| Camera                    | Fixed               | Optional pan-tilt head           |
| Sensor deck               | Minimal             | Dedicated top deck for LiDAR / RealSense |
| Battery                   | Exposed / basic     | Enclosed bay + easy swap         |
| Cable management          | Limited             | Internal channels + covers       |
| Wheel options             | Fixed               | 65–80 mm, multiple tire styles   |
| Status                    | Optional OLED       | Front light bar + status LEDs    |
| Compute mounting          | Nano-era            | Orin Nano Super / Orin NX ready  |
| Expandability             | Low                 | High (GPIO, USB, I2C, CSI)       |

---

## Mechanical Overview

### Overall Size (approx)
- Length: 220–240 mm  
- Width: 180–200 mm  
- Height (no camera): ~110 mm  
- Height with pan-tilt: ~160–180 mm  

### Core Modules
1. **Base / Drivetrain** – differential drive, motor mounts, caster or dual rear
2. **Body / Mid shell** – battery bay, compute tray, cable channels
3. **Top Deck** – flat modular plate for sensors
4. **Head (optional)** – pan-tilt camera module
5. **Front Bumper / Light bar** – status LEDs + soft bumper

### Recommended Print Strategy
- PETG or ABS for structural parts (motors + battery)
- PLA+ acceptable for covers and deck if not load-bearing
- 0.2 mm layer, 3–4 perimeters, 25–40% infill on structural parts

---

## Bill of Materials (JetNova Recommended)

### Must-Have
| Item                          | Qty | Notes / Example                     | Est. Cost |
|-------------------------------|-----|-------------------------------------|-----------|
| Jetson Orin Nano Super        | 1   | Dev kit                             | $250      |
| Geared DC motors (high quality) | 2 | 6–12 V, metal gears, encoder optional | $25–40 |
| Motor driver                  | 1   | Waveshare / SparkFun / custom HAT   | $15–25    |
| Wheels 70–80 mm               | 2   | Rubber tire                         | $12       |
| Caster or dual ball           | 1–2 |                                     | $5        |
| Battery 3S or PD power bank   | 1   | 3000–5000 mAh+                      | $25–40    |
| CSI or USB camera             | 1   | Pi Cam 3 or equivalent              | $20–35    |
| 3D printed parts              | –   | See print list                      | $15–25 filament |

### Strongly Recommended Upgrades
| Item                    | Why                                      |
|-------------------------|------------------------------------------|
| Pan-tilt kit (2× servo) | Makes following & “looking” dramatically better |
| Intel RealSense D435i   | Depth + better mapping                   |
| RPLidar A1 / A2         | Proper SLAM                              |
| Addressable LED strip   | Front light bar + status                 |
| Small OLED / e-ink      | Battery + mode display                   |

---

## Printable Parts List (target)

**Base**
- `base_left.stl` / `base_right.stl` or single `base_plate.stl`
- `motor_mount_l.stl` / `motor_mount_r.stl`
- `caster_mount.stl`

**Body**
- `battery_bay.stl` + `battery_cover.stl`
- `compute_tray_orin.stl`
- `side_covers_l/r.stl`
- `cable_cover_top.stl`

**Deck & Head**
- `top_deck.stl` (grid of M2/M3 holes)
- `pan_tilt_base.stl`
- `camera_cage_pi.stl` / `camera_cage_realsense.stl`

**Styling**
- `front_bumper.stl`
- `light_bar_diffuser.stl`
- `rear_cover.stl`

> Exact STLs are community-contributed / parametric (FreeCAD / Onshape).  
> The software does **not** hard-code any of these dimensions.

---

## Software Support (Multi-Design)

The code is no longer locked to one chassis.

```python
from jetbot.config import RobotConfig
from jetbot.modern_robot import Robot

# Classic JetBot
cfg = RobotConfig.classic()

# JetNova defaults
cfg = RobotConfig.jetnova()

# Fully custom
cfg = RobotConfig(
    name="my_bot",
    wheel_diameter_mm=75,
    wheel_base_mm=165,
    max_speed=0.45,
    motor_driver="adafruit",   # or "waveshare", "sparkfun", "custom"
    has_pan_tilt=True,
    has_lidar=False,
)

robot = Robot(config=cfg)
```

Demos automatically pick up the active config.

---

## Why JetNova Exists

Indie makers kept saying the original chassis looked dated and limited expansion.  
JetNova gives a clear, cooler target design while keeping every line of the upgraded software usable on the classic robot too.

You can:
- Build classic JetBot and run everything
- Build JetNova and get the better looks + modularity
- Mix parts (classic base + new top deck, etc.)

---

## Next Design Assets Needed (community)

- Parametric FreeCAD / Onshape source
- STEP files for the main assemblies
- Exploded assembly diagrams
- Wiring diagram (Orin + motor driver + camera + optional LiDAR)
- Short “print & build in one weekend” guide

Contributions welcome. The software is ready for multiple designs today.