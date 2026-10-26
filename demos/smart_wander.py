#!/usr/bin/env python3
"""
Smart Wander – looks intentional instead of random bouncing.

Indie demo goals:
- Robot explores the space
- Avoids obstacles using simple vision (or random if no camera)
- Occasionally pauses / looks around so it feels alive
- Easy to extend with better detection later

Usage:
  python3 demos/smart_wander.py
  python3 demos/smart_wander.py --no-camera   # pure random walk
"""

import argparse
import time
import random
import cv2
import numpy as np
import sys
sys.path.insert(0, "..")

from jetbot.modern_robot import Robot


def is_obstacle_ahead(frame, threshold=0.35):
    """Very simple center-region brightness / edge heuristic.
    Replace later with a real depth or trained model."""
    h, w = frame.shape[:2]
    # Look at lower-center region
    roi = frame[int(h*0.5):int(h*0.9), int(w*0.3):int(w*0.7)]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # High variance or dark regions often mean nearby objects / edges
    edges = cv2.Canny(gray, 50, 150)
    edge_ratio = np.count_nonzero(edges) / edges.size
    return edge_ratio > threshold


def wander_loop(robot, use_camera=True, speed=0.28):
    cap = None
    if use_camera:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("No camera – falling back to random walk")
            use_camera = False

    print("Smart wander started. Ctrl+C to stop.")
    try:
        while True:
            obstacle = False
            if use_camera:
                ret, frame = cap.read()
                if ret:
                    obstacle = is_obstacle_ahead(frame)
                    # Optional debug window
                    color = (0, 0, 255) if obstacle else (0, 255, 0)
                    cv2.putText(frame, "OBSTACLE" if obstacle else "CLEAR",
                                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                    cv2.imshow("Smart Wander", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            if obstacle:
                print("Obstacle detected → turning")
                robot.stop()
                time.sleep(0.2)
                direction = random.choice(["left", "right"])
                if direction == "left":
                    robot.left(0.35)
                else:
                    robot.right(0.35)
                time.sleep(random.uniform(0.6, 1.3))
                robot.stop()
            else:
                # Move forward a bit, sometimes with slight curve
                curve = random.uniform(-0.12, 0.12)
                robot.set_motors(speed + curve, speed - curve)
                time.sleep(random.uniform(0.8, 1.8))

                # Occasional "look around" pause so it feels alive
                if random.random() < 0.18:
                    robot.stop()
                    print("Looking around...")
                    time.sleep(random.uniform(0.5, 1.2))
                    if random.random() < 0.5:
                        robot.left(0.3)
                        time.sleep(0.4)
                        robot.stop()

    except KeyboardInterrupt:
        pass
    finally:
        robot.stop()
        if cap:
            cap.release()
        cv2.destroyAllWindows()
        print("Wander stopped.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-camera", action="store_true")
    parser.add_argument("--speed", type=float, default=0.28)
    args = parser.parse_args()

    robot = Robot()
    wander_loop(robot, use_camera=not args.no_camera, speed=args.speed)


if __name__ == "__main__":
    main()
