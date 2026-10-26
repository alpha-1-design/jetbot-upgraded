# JetBot Upgraded – Demos

These are designed to be **impressive, reliable, and easy to run**.

## Quick Launch

```bash
./demo.sh follow          # Follow people with YOLO
./demo.sh find --target cup
./demo.sh wander          # Looks like it’s exploring on purpose
./demo.sh voice           # Voice commands
./demo.sh voice --keyboard
./demo.sh dashboard       # Drive from your phone
```

## Demo Guide

### 1. YOLO Follow (`yolo_follow.py`)
The classic crowd-pleaser.  
Robot detects a target class and keeps it centered while moving forward.

```bash
python3 demos/yolo_follow.py
python3 demos/yolo_follow.py --target cat
python3 demos/yolo_follow.py --target sports_ball --speed 0.2
```

### 2. Find Object (`find_object.py`)
Robot spins looking for something, then drives toward it and stops at a nice distance.

Great for “go find the cup / bottle / person”.

### 3. Smart Wander (`smart_wander.py`)
Autonomous exploration that tries not to look random.  
Uses a simple vision heuristic for obstacles + occasional “look around” pauses.

### 4. Voice Control (`voice_control.py`)
Say (or type) commands: forward, back, left, right, stop, spin, follow.

```bash
python3 demos/voice_control.py --keyboard   # no microphone needed
```

### 5. Web Dashboard (`web_dashboard.py`)
Live camera + big touch buttons.  
Open the page on your phone and drive the robot around.

## Tips for Great Demo Videos

- Good lighting helps YOLO a lot
- Start with `yolov8n.pt` (fast)
- Use a relatively clear floor
- Record from a third-person angle + occasionally show the phone screen
- The “find the cup” and “follow me” demos are especially shareable

## Extending

All demos use `jetbot.modern_robot.Robot`.  
You can copy any of these files and build your own behavior in an evening.
