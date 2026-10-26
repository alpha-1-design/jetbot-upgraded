# Video Resources – Watch Instead of Just Reading

Curated YouTube videos that explain the concepts better than text alone.  
Watch these while (or before) you build.

---

## 1. Overall JetBot / Robot Assembly

| Topic | Video | Why watch it |
|-------|-------|--------------|
| Classic JetBot assembly (detailed) | [Assembling the NVIDIA Jetson Nano "JetBot"](https://www.youtube.com/watch?v=5trtRUhyeVI) (Hackster, ~58 min) | Full build walkthrough with real maker commentary |
| Waveshare JetBot step-by-step | [Waveshare Jetbot Build - Hardware Assembly](https://www.youtube.com/watch?v=YfqKWalPpOw) (JetsonHacks, ~20 min) | Clear timestamps for every step |
| NVIDIA official intro + hardware | [Jetson AI Fundamentals – JetBot Intro and Hardware](https://www.youtube.com/watch?v=9Wv9A6C6U5w) (NVIDIA Developer) | Good overview of the original design |
| ExplainingComputers overview | [NVIDIA JetBot: Jetson Nano Vision-Controlled AI Robot](https://www.youtube.com/watch?v=wKMWjIKaU68) | Excellent high-level demo + concepts |
| SparkFun kit assembly | [SparkFun JetBot Assembled](https://www.youtube.com/watch?v=9KCGMeMxucQ) | Short, clean kit build |

---

## 2. Motor Driver & Differential Drive (the “muscles + nervous system”)

| Topic | Video | Why watch it |
|-------|-------|--------------|
| L298N complete beginner tutorial | [Arduino DC Motor Control Tutorial - L298N](https://www.youtube.com/watch?v=I7IFsQ4tQU8) (How To Mechatronics) | Clear explanation of H-bridge + PWM |
| Deep dive on L298N + robot car | [Controlling DC Motors with the L298N H Bridge](https://www.youtube.com/watch?v=dyjo_ggEtVU) (DroneBot Workshop, ~37 min) | One of the best long-form explanations |
| Modern L298N wiring + code | [L298N Motor Driver: Control 2 DC Motors](https://www.youtube.com/watch?v=dv7U87f37ZM) (Rachel De Barros) | Very beginner-friendly, recent |

**Key concept these videos teach**: why you need a motor driver, how PWM controls speed, and how left/right motors create turning.

---

## 3. Jetson Brain Setup

| Topic | Video | Why watch it |
|-------|-------|--------------|
| Official Orin Nano getting started | [Getting Started with the Jetson Orin Nano Developer Kit](https://www.youtube.com/watch?v=VWdJ4BCtam8) (NVIDIA) | Short official overview |
| Complete Orin Nano Super setup | [NVIDIA Jetson Orin Nano Super COMPLETE Setup Guide](https://www.youtube.com/watch?v=-PjMC0gyH9s) (Bijan Bowen, ~56 min) | Very thorough modern setup |
| Another solid Orin Nano start | [Getting Started with NVIDIA Jetson Orin Nano Dev Kit](https://www.youtube.com/watch?v=NAdXA2IsZAM) | Practical first-boot walkthrough |

---

## 4. Vision / YOLO / Object Following

| Topic | Video | Why watch it |
|-------|-------|--------------|
| YOLOv8 detection + tracking | [Yolov8 object detection + deep sort object tracking](https://www.youtube.com/watch?v=jIRRuGN0j5E) | Good intro to detection + tracking pipeline |
| Custom YOLOv8 training & tracking | [YOLOv8 custom object detection and tracking](https://www.youtube.com/watch?v=-CGr7ryOH98) | If you later want to train your own objects |
| General YOLOv8 object detection | Search “YOLOv8 ultralytics tutorial” on YouTube | Official Ultralytics channel + many clear short demos |

These help you understand what the `./demo.sh follow` and `./demo.sh find` demos are actually doing under the hood.

---

## 5. Extra Useful Concepts

- **Differential drive explained** – search “differential drive robot kinematics” for short animations
- **CSI vs USB camera on Jetson** – JetsonHacks channel has several practical camera videos
- **Power systems for robots** – look for “robot battery BEC explained” or “why separate motor power”

---

## Suggested Watching Order for Absolute Beginners

1. ExplainingComputers JetBot overview (big picture)
2. One L298N motor driver video (understand the muscles)
3. NVIDIA or Bijan Bowen Jetson setup video (brain)
4. One Waveshare or Hackster assembly video (put it together)
5. A short YOLOv8 detection demo (the “eyes + brain” magic)

Then come back and run:
```bash
./demo.sh build          # interactive text assistant
./demo.sh dashboard      # first real movement
./demo.sh follow         # first intelligent behavior
```

---

**Note**: Video quality and availability can change. If a link breaks, search the title on YouTube — most of these are well-known in the community.