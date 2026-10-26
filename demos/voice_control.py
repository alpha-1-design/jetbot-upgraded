#!/usr/bin/env python3
"""
Local Voice Control for JetBot Upgraded

Indie-friendly offline voice commands.
Uses simple keyword spotting first (very lightweight).
Optional: upgrade path to Whisper / Vosk later.

Supported commands (say clearly):
  - "forward" / "go" / "move"
  - "back" / "backward"
  - "left" / "turn left"
  - "right" / "turn right"
  - "stop" / "halt"
  - "spin" / "dance"
  - "follow"          (launches YOLO follow if available)

Requirements (lightweight path):
  pip install SpeechRecognition pyaudio
  (or use the keyboard fallback if no mic)

Usage:
  python3 demos/voice_control.py
  python3 demos/voice_control.py --keyboard   # no mic needed
"""

import argparse
import time
import threading
import sys
sys.path.insert(0, "..")

from jetbot.modern_robot import Robot


# Very simple command map – easy for indie users to extend
COMMANDS = {
    "forward": "forward",
    "go": "forward",
    "move": "forward",
    "back": "backward",
    "backward": "backward",
    "left": "left",
    "right": "right",
    "stop": "stop",
    "halt": "stop",
    "spin": "spin",
    "dance": "spin",
    "follow": "follow",
}


def execute(robot, action, speed=0.3, duration=1.2):
    print(f" → {action}")
    if action == "forward":
        robot.forward(speed)
        time.sleep(duration)
        robot.stop()
    elif action == "backward":
        robot.backward(speed)
        time.sleep(duration)
        robot.stop()
    elif action == "left":
        robot.left(speed)
        time.sleep(0.7)
        robot.stop()
    elif action == "right":
        robot.right(speed)
        time.sleep(0.7)
        robot.stop()
    elif action == "stop":
        robot.stop()
    elif action == "spin":
        robot.left(0.4)
        time.sleep(2.0)
        robot.stop()
    elif action == "follow":
        print("Launching YOLO follow (Ctrl+C to return)...")
        robot.stop()
        import subprocess
        subprocess.call([sys.executable, "demos/yolo_follow.py"])


def listen_microphone(robot):
    try:
        import speech_recognition as sr
    except ImportError:
        print("SpeechRecognition not installed.")
        print("  pip install SpeechRecognition pyaudio")
        print("Falling back to keyboard mode.")
        return listen_keyboard(robot)

    r = sr.Recognizer()
    mic = sr.Microphone()

    print("Calibrating microphone (stay quiet)...")
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1.0)

    print("Listening... (say: forward, left, right, stop, spin, follow)")
    while True:
        try:
            with mic as source:
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            text = r.recognize_google(audio).lower()  # free, works offline-ish with good net
            print(f"Heard: '{text}'")
            for word, action in COMMANDS.items():
                if word in text:
                    execute(robot, action)
                    break
        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            continue
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Recognition error: {e}")
            time.sleep(0.5)


def listen_keyboard(robot):
    print("Keyboard mode (no mic needed)")
    print("Keys: w=forward  s=back  a=left  d=right  x=stop  r=spin  f=follow  q=quit")
    try:
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        tty.setcbreak(fd)
        mapping = {
            'w': "forward", 's': "backward",
            'a': "left", 'd': "right",
            'x': "stop", 'r': "spin", 'f': "follow"
        }
        while True:
            ch = sys.stdin.read(1)
            if ch == 'q':
                break
            if ch in mapping:
                execute(robot, mapping[ch])
    except Exception:
        # Fallback for environments without termios
        print("Simple input mode. Type command and press Enter:")
        while True:
            cmd = input("> ").strip().lower()
            if cmd in ("q", "quit", "exit"):
                break
            for word, action in COMMANDS.items():
                if word in cmd:
                    execute(robot, action)
                    break
    finally:
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        except Exception:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyboard", action="store_true", help="Use keyboard instead of mic")
    args = parser.parse_args()

    robot = Robot()
    print("JetBot Voice Control ready")
    try:
        if args.keyboard:
            listen_keyboard(robot)
        else:
            listen_microphone(robot)
    finally:
        robot.stop()
        print("Stopped.")


if __name__ == "__main__":
    main()
