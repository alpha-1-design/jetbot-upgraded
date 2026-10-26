# No Fancy NVIDIA Hardware Required

This project is written so you can learn and experiment **without** a Jetson, Isaac Sim, or a finished robot.

## What works on a normal computer

| Feature | Works offline / laptop? | Notes |
|---------|-------------------------|--------|
| Interactive build assistant | Yes | `./demo.sh build` |
| All written guides + YouTube links | Yes | `docs/build/`, `docs/STUDENTS_AND_EDUCATORS.md` |
| Pure-Python digital twin | Yes | `simulation/kinematics_twin.py` + unit tests |
| YOLO demos with webcam | Yes | Install `ultralytics` + OpenCV; uses camera 0 |
| Voice / keyboard control logic | Yes | `--keyboard` mode, dummy motors |
| Web dashboard code | Yes | UI runs; motors stay dummy without hardware |
| JetNova design docs | Yes | Planning / learning only until you build |

## What needs extra hardware (and when)

| Goal | Minimum hardware |
|------|------------------|
| Robot actually drives | 2 motors + motor driver + any brain (Pi, Jetson, even Arduino bridge) + power |
| Onboard YOLO + phone control | Jetson (Nano / Orin) recommended; Pi possible with limits |
| Pretty 3D physics sim | Isaac Sim on a GPU workstation (optional) |

## Design rules we follow so this stays true

1. **Dummy motors** – if the Motor HAT / driver is missing, the robot object still runs
2. **Config, not hard-coding** – classic / JetNova / custom geometry
3. **Vision is optional** – motion and skills don’t require a camera
4. **Twin first** – behaviors can be developed against the kinematics twin
5. **Clear “use what you have” paths** – see Interactive Build Guide

## Suggested order if your desk is empty

1. Read `docs/build/INTERACTIVE_BUILD_GUIDE.md` and watch 1–2 videos from `VIDEO_RESOURCES.md`
2. Run the twin tests:  
   `python3 simulation/tests/test_kinematics_twin.py`
3. Run the build assistant:  
   `./demo.sh build`
4. Optional: try YOLO on your laptop webcam
5. Only then buy or scavenge motors / a camera / a Jetson

You are not blocked. The “fancy” stack is an upgrade path, not a gate.
