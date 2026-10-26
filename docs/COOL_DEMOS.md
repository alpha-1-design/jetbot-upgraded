# Cool Stuff Indie Makers Can Build

Ordered from “weekend project” to “impressive portfolio piece”.

## Level 1 – Instant Gratification (ready now)

| Demo | Command | Status |
|------|---------|--------|
| Web Dashboard | `./demo.sh dashboard` | ✅ Done |
| YOLO person / object following | `./demo.sh follow` | ✅ Done |
| Smart Wander | `./demo.sh wander` | ✅ Done |

These three alone make a great demo video.

## Level 2 – “Wow, it actually works” (ready now)

| Demo | Command | Status |
|------|---------|--------|
| Object-specific following | `./demo.sh follow --target cat` | ✅ Done |
| Find the object | `./demo.sh find --target cup` | ✅ Done |
| Voice commands | `./demo.sh voice` / `--keyboard` | ✅ Done |

## Level 3 – Portfolio / Serious Fun (next targets)

- Room mapping with nvblox / RealSense
- Better autonomous navigation (Nav2)
- Simple LLM / natural language brain
- Pan-tilt camera head
- Status OLED + battery monitoring
- “Skills” system so behaviors can be shared

## Level 4 – Community & Sharing

- Package a trained behavior so other people can download and run it
- One-click demo mode for makerspaces / schools
- Clear “I built this in a weekend” guides

## Design Principles

1. **Demo reliability > peak cleverness**
2. **Phone-first control**
3. **Graceful degradation** (works with just camera + motors)
4. **Offline capable**
5. **Video-friendly** (clear visual feedback)
