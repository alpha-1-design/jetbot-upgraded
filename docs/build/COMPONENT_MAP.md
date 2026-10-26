# Component Map – How Everything Fits Together

Visual and functional map of a working robot (classic or JetNova).

## Physical Layout (top view concept)

```
                    [ Camera / Pan-Tilt Head ]
                              |
              +---------------+---------------+
              |         TOP DECK / LID        |
              |   (optional LiDAR / sensors)  |
              +---------------+---------------+
              |                               |
     Left     |          JETSON BRAIN         |     Right
     Motor ---|--- Motor Driver (HAT/L298N) --|--- Motor
              |                               |
              |        BATTERY BAY            |
              +-------------------------------+
                     Front Caster / Bumper
```

## Signal & Power Paths

### Power
```
Motor Battery  ──►  Motor Driver  ──►  Left Motor
                                  └──►  Right Motor

Brain Battery / PD  ──►  Jetson
```

### Control Signals
```
Jetson (I2C / GPIO / USB)  ──►  Motor Driver  ──►  Motors
Jetson  ◄──  Camera (CSI or USB)
Jetson  ◄──  Optional LiDAR / IMU
Phone   ◄──Wi-Fi──►  Jetson (web dashboard)
```

## Software Layers

```
 demos/                 (follow, find, wander, voice, dashboard)
    │
 jetbot/modern_robot.py + config.py + skills.py
    │
 Motor driver process / I2C / serial
    │
 Physical motors
```

## What Each Major Piece Is Responsible For

| Piece          | Responsibility                              | Fails if…                          |
|----------------|---------------------------------------------|------------------------------------|
| Chassis        | Keeps geometry stable                       | Wheels not parallel, tips over     |
| Motors+Wheels  | Produce movement                            | No torque, wrong voltage           |
| Motor Driver   | Amplify brain signals safely                | Wrong wiring, shared ground issues |
| Jetson         | Perception + decision making                | Overheat, brown-out, bad image     |
| Camera         | Provide visual input                        | Loose cable, wrong focus, dark     |
| Battery        | Energy for brain and/or motors              | Voltage sag under load             |
| Software       | Turn images into motor commands             | Dependencies missing, wrong config |

## Minimal Working Combinations

1. **Desk test (no robot)**  
   Laptop + webcam → run YOLO demos

2. **Rolling prototype**  
   Any chassis + 2 motors + L298N + Jetson/Pi + USB camera + 2 power sources

3. **Proper indie build**  
   JetNova or classic printed chassis + Orin Nano Super + Motor HAT + Pi Cam 3 + good battery

4. **High-capability**  
   Above + RealSense or LiDAR + pan-tilt head

Use the Interactive Build Guide and the Build Assistant to decide which combination matches what you have today.
