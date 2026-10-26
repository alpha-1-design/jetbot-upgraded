#!/usr/bin/env python3
"""
"Find the Object" – simple search + approach behavior.

Indie wow factor:
  Robot turns in place looking for a target class (person, cup, bottle...).
  When it sees one, it drives toward it and stops at a reasonable distance.

Usage:
  python3 demos/find_object.py
  python3 demos/find_object.py --target cup
  python3 demos/find_object.py --target bottle --conf 0.4
"""

import argparse
import time
import cv2
import sys
sys.path.insert(0, "..")

from jetbot.modern_robot import Robot

try:
    from ultralytics import YOLO
except ImportError:
    print("Need ultralytics:  pip install ultralytics")
    raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="yolov8n.pt")
    parser.add_argument("--target", default="cup")
    parser.add_argument("--conf", type=float, default=0.4)
    parser.add_argument("--speed", type=float, default=0.22)
    args = parser.parse_args()

    model = YOLO(args.model)
    names = model.names
    target_ids = [k for k, v in names.items() if v == args.target]
    if not target_ids:
        print("Available classes:", list(names.values()))
        raise SystemExit(f"Unknown target: {args.target}")
    target_id = target_ids[0]

    robot = Robot()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No camera")
        return

    print(f"Searching for '{args.target}'... (Ctrl+C to stop)")
    state = "search"          # search → approach → done
    lost_count = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            h, w = frame.shape[:2]
            results = model(frame, conf=args.conf, verbose=False)[0]

            best = None
            best_area = 0
            for box in results.boxes:
                if int(box.cls[0]) != target_id:
                    continue
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                area = (x2 - x1) * (y2 - y1)
                if area > best_area:
                    best_area = area
                    best = (x1, y1, x2, y2)

            if best is not None:
                lost_count = 0
                x1, y1, x2, y2 = best
                cx = (x1 + x2) / 2
                area_ratio = best_area / (w * h)
                error = (cx - w/2) / (w/2)

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"{args.target} {area_ratio:.2f}", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                if area_ratio > 0.18:          # close enough
                    robot.stop()
                    cv2.putText(frame, "FOUND!", (20, 90),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)
                    state = "done"
                else:
                    # Approach while centering
                    turn = -error * 0.55
                    left = args.speed + turn
                    right = args.speed - turn
                    robot.set_motors(max(-0.4, min(0.4, left)),
                                     max(-0.4, min(0.4, right)))
                    state = "approach"
            else:
                lost_count += 1
                if state == "approach" and lost_count < 8:
                    # brief patience
                    robot.stop()
                else:
                    # Search: slow spin
                    robot.left(0.25)
                    state = "search"
                    cv2.putText(frame, "Searching...", (20, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)

            cv2.imshow("Find Object", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if state == "done":
                time.sleep(2.0)   # celebrate
                # Optional: go back to search
                state = "search"

    except KeyboardInterrupt:
        pass
    finally:
        robot.stop()
        cap.release()
        cv2.destroyAllWindows()
        print("Done.")


if __name__ == "__main__":
    main()
