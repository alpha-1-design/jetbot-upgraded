# JetBot Upgraded (2026)

**The indie-friendly modern reboot of NVIDIA’s classic open-source AI robot.**

Original JetBot (2019) was great for its time.  
This version is rebuilt for what independent makers actually want in 2026:

- Cool, reliable demos that look good on video
- Modern Jetson boards (Orin Nano Super / Orin NX) — **optional**
- Phone-based control + live camera
- YOLO object following that just works
- Clear path from “weekend project” → serious robot
- ROS 2 + Isaac ROS when you’re ready for mapping & real navigation

---

## You do **not** need fancy NVIDIA hardware to start

Most of this project runs on a normal laptop or PC.

| What you want to do | Need Jetson? | Need Isaac Sim? | What to run |
|---------------------|--------------|-----------------|-------------|
| Learn the system / read guides | No | No | Docs + `./demo.sh build` |
| Test robot motion logic | No | No | `python3 simulation/tests/test_kinematics_twin.py` |
| Try vision (YOLO) | No | No | Laptop webcam + `demos/yolo_follow.py` |
| Drive a real robot from your phone | Jetson *or* Pi + motors | No | `./demo.sh dashboard` |
| Full 3D digital twin | No | Yes (optional) | Isaac Sim script |

- No motor HAT / no robot → code uses **dummy motors** (safe, nothing crashes)
- No camera → skip vision demos; twin + docs still work
- No 3D printer → cardboard, foam, toy-car parts are documented

Start with what you have. Add Jetson / better parts later if you want.

---

## Start Here (Indie Path)

### 1. Read the Indie Guide
→ [`docs/INDIE_GUIDE.md`](docs/INDIE_GUIDE.md)

### 2. See the Cool Stuff You Can Build
→ [`docs/COOL_DEMOS.md`](docs/COOL_DEMOS.md)

### 3. Run the Best Demos

```bash
./demo.sh dashboard      # drive from your phone
./demo.sh follow         # YOLO person / object following
./demo.sh find --target cup
./demo.sh wander
./demo.sh voice --keyboard
./demo.sh build          # interactive build assistant
```

---

## Recommended Hardware (2026)

| Priority | Item                        | Notes                              |
|----------|-----------------------------|------------------------------------|
| Must     | Jetson Orin Nano Super      | Best price/performance             |
| Must     | Chassis (Waveshare / print) | Original STLs still work           |
| Must     | Good camera (CSI or USB)    | Pi Cam 3 or RealSense              |
| Nice     | RPLidar or similar          | Unlocks real mapping               |
| Nice     | Better battery + regulator  | Avoid brownouts                    |

Full details: [`docs/hardware_upgrade.md`](docs/hardware_upgrade.md)

---

## Project Structure

```
jetbot/                 # Core library (original + modern_robot.py)
demos/                  # Cool, ready-to-run demos (start here)
simulation/             # Digital twin (kinematics + Isaac Sim)
  ├── kinematics_twin.py
  └── isaac_sim/jetbot_twin.py
docs/
  ├── INDIE_GUIDE.md
  ├── COOL_DEMOS.md
  ├── STUDENTS_AND_EDUCATORS.md
  ├── build/            # Interactive assembly + video resources
  ├── designs/          # JetNova
  └── simulation/       # Isaac Sim twin guide
ros2/                   # ROS 2 skeleton
docker/modern/
notebooks/
tools/build_assistant.py
```

---

## Philosophy

- **Demo reliability > peak cleverness**
- Phone-first control
- Works offline
- Graceful fallbacks (dummy motors if no hardware)
- Easy to go deeper (ROS 2 / Isaac) later
- Make things that look good when people film them

---

## Status

| Feature                     | State          |
|----------------------------|----------------|
| Modern robot abstraction   | Done           |
| Web dashboard              | Done           |
| YOLO following demo        | Done           |
| Find-object demo           | Done           |
| Smart wander               | Done           |
| Voice commands             | Done           |
| One-command demo launcher  | Done (`./demo.sh`) |
| Indie + Cool Demos docs    | Done           |
| Interactive build guide + videos | Done     |
| Student & educator path    | Done           |
| JetNova design path        | Done           |
| Hardware upgrade guide     | Done           |
| ROS 2 packages             | Skeleton       |
| Isaac Sim digital twin     | Done (kinematics tested + Isaac script) |

---

## License

MIT (same as original JetBot)

**Original project**: https://github.com/NVIDIA-AI-IOT/jetbot  
**This version**: Rebuilt for indie makers and modern Jetson hardware.
