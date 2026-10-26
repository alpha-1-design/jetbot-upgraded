# JetBot Upgraded – Indie Maker Guide

This is for independent makers, students, and hobbyists who want a **cool, capable, affordable robot** they can actually build and show off.

## What Indie People Usually Want

1. **It looks and moves cool** – not a slow wobbling brick
2. **Impressive demos** that work reliably (object following, voice commands, autonomous wandering, “it understands me”)
3. **Doesn’t require a PhD** to get started
4. **Can be extended** – add a camera arm, LiDAR, better brains, etc.
5. **Works offline** as much as possible
6. **Cheap enough** that breaking it doesn’t hurt too much
7. **Shares well** – easy to post videos, give demos, contribute back

## Recommended Indie Build Paths

### Path A: “Coolest on a Budget” (~$350–450 total)
- Jetson Orin Nano Super Dev Kit
- Waveshare or SparkFun JetBot chassis kit (or print the original chassis)
- Raspberry Pi Camera Module 3
- Decent 3S/4S battery + good voltage regulator
- Optional: cheap RPLidar A1 clone later

**Best demos**: YOLO object following, collision avoidance, web teleop, simple voice commands

### Path B: “Most Impressive” (~$550–700)
- Same as above + Intel RealSense D435i (or D455)
- Small LiDAR
- Better wheels + suspension if possible
- Optional OLED status screen

**Best demos**: Real 3D mapping with nvblox, autonomous navigation, “go find the red cup”, voice + vision

### Path C: “Maximum Fun / Learning”
- Start with Path A
- Spend time in simulation (Isaac Sim) first
- Train your own behaviors
- Add a simple pan-tilt camera later

## The Cool Stuff We Are Building Toward

| Feature                        | Status in this repo      | Why indie people love it                  |
|-------------------------------|--------------------------|-------------------------------------------|
| Modern web dashboard          | In progress              | Control from phone / laptop, no Jupyter pain |
| YOLO object following         | Ready to add             | Looks magical, very reliable              |
| Voice commands (local)        | Planned                  | “Hey JetBot, follow me”                   |
| Autonomous wander + avoid     | Classic + improved       | Classic crowd-pleaser                     |
| Map the room (nvblox)         | ROS 2 path               | Feels like a real robot                   |
| Simulation first              | Skeleton                 | Test ideas without risking hardware       |
| One-command demos             | Goal                     | `./demo.sh follow` just works             |
| Easy skill sharing            | Future                   | Export a behavior and give it to friends  |

## Philosophy of This Upgrade

- Keep the spirit of the original JetBot (affordable, educational, fun)
- Remove the old pain points (ancient dependencies, Nano-only, fragile notebooks)
- Make the impressive things *reachable* for one person in a garage or dorm
- Prefer things that work offline and don’t require cloud accounts
- Make it easy to go deeper (ROS 2 / Isaac) when the user is ready

## Quick Wins You Can Do This Weekend

1. Get the robot driving with the modern Docker image
2. Run the updated basic motion + teleop
3. Drop in YOLOv8 and make it follow a person or a specific object
4. Open the web dashboard from your phone and drive it around
5. Record a 30-second video — this is the best marketing for the project

## How to Contribute the Indie Way

- Improve a demo so it’s more reliable
- Add support for a popular motor driver or camera
- Make the web UI prettier or more useful
- Write a clear “I built this in one weekend” guide
- Share your trained model or behavior

This project should feel like a launchpad, not a finished product.