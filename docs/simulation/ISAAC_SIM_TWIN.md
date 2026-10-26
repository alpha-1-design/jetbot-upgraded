# Isaac Sim Digital Twin

Run JetBot / JetNova behaviors in simulation — no physical robot required.

## Two layers

| Layer | Where it runs | Purpose |
|-------|----------------|---------|
| **Kinematics twin** (`simulation/kinematics_twin.py`) | Any Python | Fast tests, CI, offline behavior dev, classrooms without GPUs |
| **Isaac Sim twin** (`simulation/isaac_sim/jetbot_twin.py`) | Isaac Sim workstation | Full physics, sensors, rendering, digital-twin fidelity |

Both expose a control API compatible with `jetbot.modern_robot.Robot`
(`forward`, `backward`, `left`, `right`, `stop`, `set_motors`).

---

## 1. Pure-Python twin (works right now)

```bash
# From repo root
python3 simulation/tests/test_kinematics_twin.py
```

```python
from simulation import KinematicsTwin, TwinConfig

twin = KinematicsTwin(TwinConfig.jetnova())
twin.forward(0.3)
twin.run(2.0)          # simulate 2 seconds
print(twin.pose())     # (x, y, theta)
```

Use this to:
- Unit-test new skills before touching hardware
- Let students experiment on laptops
- Develop control logic offline

Classic vs JetNova geometry is built in (`TwinConfig.classic()` / `.jetnova()`).

---

## 2. Isaac Sim twin (full digital twin)

### Requirements
- Isaac Sim 4.x / 5.x / 6.x (workstation with NVIDIA GPU)
- Official Jetbot USD asset (ships with Isaac Sim)

### Run

```bash
# Inside Isaac Sim environment
./python.sh simulation/isaac_sim/jetbot_twin.py

# Headless automated test
./python.sh simulation/isaac_sim/jetbot_twin.py --headless --test

# Custom motion
./python.sh simulation/isaac_sim/jetbot_twin.py --linear 0.3 --angular 0.8 --duration 15
```

The script:
1. Loads the NVIDIA Jetbot USD
2. Creates a `DifferentialController` with classic JetBot wheel geometry
3. Runs a short demo (forward → turn → forward → stop)
4. Uses the same twist → wheel mapping Isaac documents for Jetbot

### Geometry used
| Parameter | Value | Notes |
|-----------|-------|-------|
| Wheel radius | 0.0325 m | 65 mm diameter (classic) |
| Wheel base  | 0.1125 m | Isaac’s Jetbot default |

JetNova dimensions can be swapped in later by editing the controller construction (or adding a CLI flag).

---

## 3. Mapping real robot ↔ sim

```
Real hardware                     Simulation
-------------                     ----------
jetbot.modern_robot.Robot    ↔    KinematicsTwin  or  Isaac WheeledRobot + DifferentialController
set_motors(left, right)      ↔    same / or twist (v, ω)
Camera (OpenCV / CSI)        ↔    Isaac camera prim (future) or skip for kinematics-only
YOLO demos                   ↔    Run vision on host, send speeds into twin (easy bridge)
```

Recommended workflow:
1. Prototype behavior on `KinematicsTwin`
2. Validate motion in Isaac Sim
3. Deploy same logic to real `Robot`

---

## 4. What is intentionally still light

- No full sensor sim (depth / LiDAR) wired up yet
- No automatic USD exporter for a custom JetNova mesh
- Vision demos still expect a real or webcam image stream

These are natural next extensions once the motion twin is solid.

---

## 5. References (official)

- [Differential Drive Tutorial (Isaac Sim)](https://docs.isaacsim.omniverse.nvidia.com/latest/controllers/tutorial_differential_drive.html)
- [Wheeled robots / Jetbot asset](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_robots_wheeled.html)
- Example scripts under Isaac Sim:  
  `standalone_examples/api/isaacsim.robot.wheeled_robots.examples/`
