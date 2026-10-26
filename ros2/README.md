# ROS 2 + Isaac ROS Path (for when you're ready)

Most indie users should start with the pure Python demos (`demos/`).  
Come here when you want:

- Proper mapping of a room
- Autonomous navigation (“go to the kitchen”)
- Multiple sensors (camera + LiDAR + IMU)
- Integration with the wider ROS / Isaac ecosystem

## Planned Packages

```
ros2/
├── jetbot_description/     # URDF + meshes
├── jetbot_bringup/         # launch files that start everything
├── jetbot_teleop/          # gamepad + keyboard
├── jetbot_nav/             # Nav2 configuration
└── jetbot_perception/      # camera + optional YOLO / Isaac nodes
```

## Recommended Stack (2026)

- ROS 2 Jazzy or Humble
- Isaac ROS (nvblox, cuVSLAM, image pipeline)
- Nav2 for navigation
- Optional: RealSense or ZED for depth

## Why this path is powerful for indie makers

Once you have mapping + navigation working, you can build high-level behaviors very quickly:

- “Go explore and come back”
- “Patrol these waypoints”
- “Find the red cup and stop in front of it”

This is the difference between a cool demo robot and something that feels like a real home robot.