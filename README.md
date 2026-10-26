# JetBot Upgraded (2026)

**The indie-friendly modern reboot of NVIDIA’s classic open-source AI robot.**

Original JetBot (2019) was great for its time.  
This version is rebuilt for what independent makers actually want in 2026:

- Cool, reliable demos that look good on video
- Modern Jetson boards (Orin Nano Super / Orin NX)
- Phone-based control + live camera
- YOLO object following that just works
- Clear path from “weekend project” → serious robot
- ROS 2 + Isaac ROS when you’re ready for mapping & real navigation

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
  ├── yolo_follow.py    # Object following with YOLOv8
  ├── web_dashboard.py  # Phone-friendly control + video
  └── README.md
docs/
  ├── INDIE_GUIDE.md    # Written for independent makers
  ├── COOL_DEMOS.md     # What to build and in what order
  └── hardware_upgrade.md
ros2/                   # Future ROS 2 + Isaac ROS packages
docker/modern/          # JetPack 6 oriented Dockerfile
notebooks/              # Original educational notebooks (still useful)
assets/                 # 3D printable chassis files
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
| Isaac Sim digital twin     | Planned        |

---

## License

MIT (same as original JetBot)

**Original project**: https://github.com/NVIDIA-AI-IOT/jetbot  
**This version**: Rebuilt for indie makers and modern Jetson hardware.
