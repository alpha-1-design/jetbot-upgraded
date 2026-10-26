# Interactive Build Guide – Understand, Improvise, Assemble

This guide is meant to be used **while you build**.  
It explains what each part does, how pieces connect, and how to substitute things you already have around you.

> **Prefer video?**  
> See the curated list: **[VIDEO_RESOURCES.md](VIDEO_RESOURCES.md)**  
> Recommended starting videos are also linked under each major section below.

---

## Big Picture – How the Robot Works

**Watch first (big picture):**  
- [NVIDIA JetBot overview – ExplainingComputers](https://www.youtube.com/watch?v=wKMWjIKaU68)  
- [Jetson AI Fundamentals – JetBot Hardware (NVIDIA)](https://www.youtube.com/watch?v=9Wv9A6C6U5w)

Think of the robot as four layers that talk to each other:

```
┌─────────────────────────────────────────┐
│  4. BRAIN (Jetson)                      │  Sees, decides, sends motor commands
├─────────────────────────────────────────┤
│  3. NERVOUS SYSTEM (wires + driver)     │  Carries power & signals
├─────────────────────────────────────────┤
│  2. MUSCLES (motors + wheels)           │  Makes it move
├─────────────────────────────────────────┤
│  1. SKELETON (chassis + mounts)         │  Holds everything in place
└─────────────────────────────────────────┘
```

Plus sensors (camera, optional LiDAR) that feed information **up** to the brain.

If you understand this stack, every design (classic JetBot or JetNova) makes sense.

---

## Component-by-Component: What It Does & What You Can Use Instead

### 1. Brain – NVIDIA Jetson (Orin Nano Super recommended)

**Watch:**  
- [Getting Started with Jetson Orin Nano (NVIDIA official)](https://www.youtube.com/watch?v=VWdJ4BCtam8)  
- [Complete Orin Nano Super Setup Guide](https://www.youtube.com/watch?v=-PjMC0gyH9s)

**What it does**  
Runs the AI, camera code, web dashboard, and decides left/right motor speeds.

**Ideal**  
- Jetson Orin Nano Super Dev Kit

**Around-the-house / cheaper alternatives**  
- Older Jetson Nano / Xavier NX (still works, slower)
- Raspberry Pi 5 + USB Coral / Hailo (possible but different software path)
- Laptop + USB motors for pure testing (no mobile robot)

**How it connects**  
- Power: barrel jack or USB-C PD  
- Camera: CSI ribbon or USB  
- Motors: USB or GPIO/I2C → motor driver  
- Network: Wi-Fi for the phone dashboard

---

### 2. Motor Driver (the “translator”)

**Watch:**  
- [L298N Motor Driver Tutorial (How To Mechatronics)](https://www.youtube.com/watch?v=I7IFsQ4tQU8)  
- [Deep dive – L298N + robot car (DroneBot Workshop)](https://www.youtube.com/watch?v=dyjo_ggEtVU)

**What it does**  
Takes low-power signals from the Jetson and controls high-power motors safely.

**Ideal**  
- Adafruit Motor HAT / Waveshare Motor Driver HAT / SparkFun version

**Around-the-house alternatives**  
- L298N dual H-bridge module (very common, cheap)
- Two single motor drivers
- Even a small RC car ESC pair (harder to control precisely)

**How it connects**  
```
Jetson (I2C or GPIO pins)  →  Motor Driver  →  Left Motor + Right Motor
                              ↑
                           Battery power
```

---

### 3. Motors + Wheels (“muscles”)

**Watch (same motor-driver videos above also cover this):**  
Understanding differential drive is easiest by watching a robot actually turn with left/right speed differences.

**What they do**  
Turn electrical energy into rotation. Two motors = differential drive (turn by spinning sides at different speeds).

**Ideal**  
- 6–12 V geared DC motors with metal gears  
- 65–80 mm rubber wheels

**Around-the-house alternatives**  
- Motors from an old toy car / RC car  
- Continuous-rotation servos (easier wiring, lower torque)  
- Hoverboard motors (overkill and heavy, but possible)  
- Even two computer fans (only for very light demos – not practical)

**Key idea**  
As long as you can control left and right speed independently, the software works.

---

### 4. Chassis / Skeleton

**What it does**  
Holds motors, battery, Jetson, and camera in the right places so the robot doesn’t fall apart or tip over.

**Ideal**  
- 3D-printed classic JetBot or JetNova parts

**Around-the-house alternatives**  
- Foam core / corrugated plastic (Coroplast)  
- Laser-cut plywood or MDF  
- LEGO / Technic frame  
- Old robot vacuum base  
- Plastic storage container lid + hot glue (surprisingly common for prototypes)  
- Cardboard + duct tape for a same-day test chassis

**Critical measurements**  
- Motors parallel and at the same height  
- Center of gravity low and centered  
- Camera has a clear forward view

---

### 5. Camera (the “eyes”)

**What it does**  
Feeds images to YOLO / vision code so the robot can follow, avoid, or find objects.

**Ideal**  
- Raspberry Pi Camera Module 3 (CSI)  
- Or Intel RealSense (depth)

**Around-the-house alternatives**  
- Any USB webcam  
- Old phone used as IP camera (more complex)  
- Laptop webcam while testing code on a desk

**How it connects**  
- CSI ribbon → Jetson CSI port  
  or  
- USB webcam → any USB port

---

### 6. Power System

**What it does**  
Feeds the Jetson (5 V / 9–20 V depending on model) and the motors (usually 7–12 V).

**Ideal**  
- 3S LiPo + good BEC / regulator  
- or high-quality USB-C PD power bank + separate motor battery

**Around-the-house alternatives**  
- Two separate power banks (one for Jetson, one for motors)  
- Old laptop battery pack (careful with voltage)  
- AA / 18650 battery holders for light testing

**Safety rule**  
Never power motors directly from the Jetson’s 5 V pins.

---

### 7. Optional but Cool Add-ons

| Part              | What it adds                     | Cheap substitute              |
|-------------------|----------------------------------|-------------------------------|
| LiDAR             | Real mapping & better avoidance  | Ultrasonic HC-SR04 sensors    |
| Pan-tilt head     | Camera can look around           | Two hobby servos + bracket    |
| Status LEDs       | Shows mode / battery             | Single RGB LED or Neopixel    |
| OLED screen       | Text status                      | Serial print to phone         |
| Bumper            | Physical collision detect        | Limit switches or foam        |

---

## How the Pieces Go Together (Assembly Flow)

**Best videos to watch while assembling:**  
- [Waveshare JetBot Hardware Assembly (step-by-step)](https://www.youtube.com/watch?v=YfqKWalPpOw)  
- [Full JetBot assembly live build (Hackster)](https://www.youtube.com/watch?v=5trtRUhyeVI)  
- [SparkFun JetBot assembly](https://www.youtube.com/watch?v=9KCGMeMxucQ)

Follow this order – it matches how the system actually works.

### Step 1 – Skeleton + Muscles
1. Mount both motors to the chassis so the wheels are parallel.
2. Add the front caster or rear skids.
3. Spin the wheels by hand – nothing should rub.

**You should now have a rolling platform with no electronics.**

### Step 2 – Power & Driver
1. Mount the motor driver close to the motors.
2. Connect motor wires to the driver outputs.
3. Connect battery → driver power input (observe polarity!).
4. Do **not** connect to Jetson yet.

**Test**: briefly apply power – motors should be able to spin if you force the driver inputs (or wait for software).

### Step 3 – Brain
1. Mount the Jetson so ports are accessible and it gets airflow.
2. Connect Jetson power (separate from motor battery if possible).
3. Connect the control signals (I2C / GPIO / USB) from Jetson → motor driver.
4. Power on Jetson only and confirm it boots.

### Step 4 – Eyes
1. Mount camera facing forward, slightly tilted down (good for floor + people).
2. Connect CSI or USB.
3. Test with a simple camera preview before running AI demos.

### Step 5 – Software Bring-up
```bash
# On the Jetson
pip install -r requirements-demos.txt
./demo.sh dashboard     # easiest first test
```

Open the page on your phone. If the robot moves when you press buttons, the whole stack is alive.

### Step 6 – First Intelligent Behavior
```bash
./demo.sh follow
```

---

## Interactive Mental Model – “What is happening right now?”

When you run a demo, this is the loop:

```
Camera → Image → AI model (YOLO etc.) → Decision
                                         ↓
                              left_speed, right_speed
                                         ↓
                              Motor Driver → Motors → Movement
                                         ↓
                              New camera image … (repeat)
```

The web dashboard skips the AI and lets **you** set left/right speeds directly from your phone.

Voice control and skills just become different ways of choosing those speeds.

---

## “I Only Have X” Quick Recipes

**I only have a Raspberry Pi and a toy car**  
→ Tear the toy car drivetrain out, keep the motors/wheels, control them with an L298N, run the same Python demos (some speed tuning needed).

**I have no 3D printer**  
→ Foam-core or plywood base + hot glue + zip ties. Many people start this way.

**I have no special motor driver**  
→ L298N module + Arduino as a bridge, or direct GPIO with transistors (advanced).

**I just want to test the AI without building anything**  
→ Run the YOLO demos on a laptop webcam first. The vision code is the same.

---

## Visualization Tips While Building

1. Take a photo after every major step (motors on, driver on, Jetson on, camera on).  
2. Label wires with tape (L+, L−, R+, R−, 5 V, GND).  
3. Draw the power path on paper: Battery → Driver → Motors and Battery → Jetson.  
4. When something doesn’t move, ask:  
   - Does the brain have power?  
   - Does the driver have power?  
   - Are the signal wires connected?  
   - Is the software actually sending non-zero speeds?

---

## Next Interactive Tools in This Repo

- `tools/build_assistant.py` – terminal walkthrough that asks what parts you have and suggests the best path
- Component checklist you can tick off
- Simple wiring diagram descriptions for the most common combinations

Build the skeleton first. Get it rolling under manual control. Then add the eyes and the brain. That order keeps frustration low and understanding high.
