#!/usr/bin/env python3
"""
Cool Indie Demo: YOLO Object Following

What it does:
- Detects people (or any class you choose) with YOLOv8
- Steers the robot to keep the target in the center of the frame
- Very impressive for demos and surprisingly reliable on Orin Nano

Usage:
    python3 demos/yolo_follow.py                  # follow people
    python3 demos/yolo_follow.py --target cat     # follow cats
    python3 demos/yolo_follow.py --target sports_ball

Requirements:
    pip install ultralytics opencv-python
    (On Jetson, use a TensorRT-exported model for best speed)
"""

import argparse
import time
import cv2
import numpy as np

try:
    from ultralytics import YOLO
except ImportError:
    print("Please install ultralytics:  pip install ultralytics")
    raise

# Import the modern robot (falls back to dummy if no hardware)
import sys
sys.path.insert(0, "..")
from jetbot.modern_robot import Robot


def main():
    parser = argparse.ArgumentParser(description="YOLO Object Following for JetBot")
    parser.add_argument("--model", default="yolov8n.pt", help="YOLO model path")
    parser.add_argument("--target", default="person", help="Class name to follow")
    parser.add_argument("--camera", default=0, type=int, help="Camera index")
    parser.add_argument("--conf", default=0.45, type=float, help="Confidence threshold")
    parser.add_argument("--speed", default=0.25, type=float, help="Base forward speed")
    parser.add_argument("--turn-gain", default=0.6, type=float, help="How aggressively to turn")
    args = parser.parse_args()

    print(f"Loading model {args.model}...")
    model = YOLO(args.model)

    # Get class id for target
    names = model.names
    target_ids = [k for k, v in names.items() if v == args.target]
    if not target_ids:
        print(f"Available classes: {list(names.values())}")
        raise ValueError(f"Target class '{args.target}' not found")
    target_id = target_ids[0]
    print(f"Following class: {args.target} (id={target_id})")

    robot = Robot()
    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print("Could not open camera. Using dummy mode.")
        return

    print("Running... Press Ctrl+C to stop")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            h, w = frame.shape[:2]
            results = model(frame, conf=args.conf, verbose=False)[0]

            # Find the largest target of the desired class
            best = None
            best_area = 0
            for box in results.boxes:
                cls = int(box.cls[0])
                if cls != target_id:
                    continue
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                area = (x2 - x1) * (y2 - y1)
                if area > best_area:
                    best_area = area
                    best = (x1, y1, x2, y2)

            if best is not None:
                x1, y1, x2, y2 = best
                cx = (x1 + x2) / 2
                error = (cx - w / 2) / (w / 2)   # -1 .. 1

                # Simple proportional control
                turn = -error * args.turn_gain
                left = args.speed + turn
                right = args.speed - turn

                # Clamp
                left = max(-0.5, min(0.5, left))
                right = max(-0.5, min(0.5, right))
                robot.set_motors(left, right)

                # Draw for feedback
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"Following {args.target}", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                robot.stop()
                cv2.putText(frame, "Searching...", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("JetBot YOLO Follow", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        pass
    finally:
        robot.stop()
        cap.release()
        cv2.destroyAllWindows()
        print("Stopped.")


if __name__ == "__main__":
    main()
