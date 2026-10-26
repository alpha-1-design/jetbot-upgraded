# JetBot Upgraded for Students & Educators

This project is designed so **students can learn by building and seeing results quickly**, while educators get a clear progression and low-friction demos.

---

## Why it works well for students

| Student need | How this project helps |
|--------------|------------------------|
| Fast visible results | `./demo.sh dashboard` and `./demo.sh follow` work early |
| Understand the whole system | Interactive Build Guide + Component Map + videos |
| Start simple, go deeper | Clear levels: drive → vision → autonomy → (optional) ROS |
| Limited budget / parts | Explicit “use what you have” and scavenged-parts paths |
| Different skill levels | Dummy-motor mode, laptop webcam testing, full robot |
| Shareable work | Demos are short scripts students can modify and show |

---

## Suggested Learning Path (Students)

### Week / Stage 1 – Make it move
**Goal:** Understand differential drive and remote control.

- Read: Big-picture section of `docs/build/INTERACTIVE_BUILD_GUIDE.md`
- Watch: one JetBot overview video + one L298N/motor video (see `VIDEO_RESOURCES.md`)
- Do: `./demo.sh dashboard` — drive from phone
- Stretch: change speed values, add a “boost” button idea

**Learning outcomes:** motors, power vs signal, left/right control, basic debugging

### Week / Stage 2 – Give it eyes
**Goal:** Connect vision to motion.

- Run: `./demo.sh follow` and `./demo.sh find --target cup`
- Change the target class, confidence, speed
- Optional: run YOLO on a laptop webcam first (no robot needed)

**Learning outcomes:** camera pipeline, object detection, simple control from vision

### Week / Stage 3 – Make it behave
**Goal:** Autonomous and interactive behaviors.

- `./demo.sh wander`
- `./demo.sh voice --keyboard` (then try mic if available)
- Modify or combine skills in `jetbot/skills.py`

**Learning outcomes:** state machines / simple behaviors, human–robot interaction

### Week / Stage 4 – Design & systems thinking
**Goal:** Own the full stack.

- Use `./demo.sh build` (assistant) and the Component Map
- Compare classic vs JetNova design goals (`docs/designs/`)
- Propose one improvement (mechanical, software, or new demo)

**Learning outcomes:** system architecture, trade-offs, documentation

### Optional advanced track
- ROS 2 / Isaac path (`ros2/` notes)
- Custom YOLO training
- Mapping / navigation concepts
- Simulation (future Isaac Sim path)

---

## For Educators – Classroom & Lab Tips

### Low-friction first success
Start every group with:
```bash
./demo.sh dashboard
```
If the robot moves from a phone, confidence goes up immediately.

### Hardware strategies
- **Shared robots:** one or two working platforms + many students doing vision/code on laptops
- **Bring-your-own-parts:** encourage scavenged motors/chassis; software still works
- **No robot day:** pure vision demos with webcams still teach the AI concepts

### Assessment ideas
- Demo video (30–60 s) of follow or find-object
- Short written explanation: “What happens from camera frame to motor command?”
- Modification challenge: change behavior or add a simple new skill
- Design rationale: why they chose certain parts or geometry

### Safety & practical notes
- Separate motor power from the Jetson when possible
- Secure batteries; no loose LiPos in bags
- Clear emergency stop (dashboard STOP + physical power)
- Supervise first power-on of any scavenged motor setup

### Group roles (optional)
- Mechanical / chassis
- Electrical / wiring & power
- Software / demos & tuning
- Documentation / video & explanation

Rotate roles so everyone touches the full stack.

---

## Quick map: existing docs → student use

| Resource | Best for students |
|----------|-------------------|
| `./demo.sh build` | Self-paced “what do I have / what do I do next” |
| `docs/build/INTERACTIVE_BUILD_GUIDE.md` | Understanding parts + assembly order |
| `docs/build/VIDEO_RESOURCES.md` | Visual learners / flipped classroom |
| `docs/build/COMPONENT_MAP.md` | System diagram for reports or exams |
| `docs/COOL_DEMOS.md` | Project inspiration and difficulty ladder |
| `docs/designs/JETNOVA.md` | Design thinking / “improve the robot” assignments |
| `demos/` + `jetbot/skills.py` | Coding exercises that stay small and visual |

---

## One-page student checklist

- [ ] I can drive the robot from a phone (`dashboard`)
- [ ] I can explain what the motor driver does
- [ ] I can run object following and change the target
- [ ] I know the path: Camera → AI → speeds → motors
- [ ] I tried at least one autonomous or voice behavior
- [ ] I can point to one thing I would improve next

---

This keeps the same codebase useful for hobbyists **and** structured learning.  
Students get fast wins; educators get a progression without writing a full curriculum from scratch.
