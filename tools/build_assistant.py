#!/usr/bin/env python3
"""
Interactive Build Assistant for JetBot Upgraded / JetNova

Walks a user through what they have, explains each component,
and recommends the simplest path to a working robot.
"""

import sys


def ask(question: str, options=None):
    print()
    print(question)
    if options:
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        while True:
            raw = input("Choose number (or type answer): ").strip()
            if raw.isdigit() and 1 <= int(raw) <= len(options):
                return options[int(raw) - 1]
            if raw:
                return raw
    return input("> ").strip()


def yes_no(question: str) -> bool:
    ans = ask(question + " (y/n)").lower()
    return ans.startswith("y")


def header(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    header("JetBot / JetNova Interactive Build Assistant")
    print(
        "I'll help you understand the components, use what you already have,\n"
        "and assemble a working robot step by step.\n"
    )

    # ---- Inventory ----
    header("1. What do you already have?")

    has_jetson = yes_no("Do you have any NVIDIA Jetson board (Nano / Orin / Xavier)?")
    has_pi = yes_no("Do you have a Raspberry Pi?") if not has_jetson else False
    has_motors = yes_no("Do you have two DC motors or a toy car you can scavenge?")
    has_driver = yes_no("Do you have a motor driver (L298N, Motor HAT, etc.)?")
    has_camera = yes_no("Do you have any camera (USB webcam, Pi Cam, phone)?")
    has_printer = yes_no("Do you have access to a 3D printer?")
    has_battery = yes_no("Do you have a battery pack or power bank?")

    # ---- Brain recommendation ----
    header("2. Brain Recommendation")
    if has_jetson:
        print("✓ Great – use your Jetson as the brain.")
        print("  Preferred: Orin Nano Super > Orin NX > Nano")
        brain = "jetson"
    elif has_pi:
        print("• You can prototype vision and control logic on the Raspberry Pi.")
        print("  For full YOLO performance a Jetson is still recommended later.")
        brain = "pi"
    else:
        print("• Start by testing the AI demos on a normal laptop/webcam.")
        print("  Buy or borrow a Jetson when you are ready for a mobile robot.")
        brain = "laptop"

    # ---- Motion ----
    header("3. Motion System")
    if has_motors and has_driver:
        print("✓ You already have the core of the muscle system.")
        print("  Make sure you can control left and right motors independently.")
    elif has_motors and not has_driver:
        print("• Motors without a driver → get an L298N module (very common & cheap).")
        print("  It becomes the translator between brain signals and motor power.")
    else:
        print("• Scavenge two motors + wheels from an old toy car or buy a cheap pair.")
        print("  Add an L298N or Motor HAT so the brain can control them safely.")

    # ---- Chassis ----
    header("4. Skeleton (Chassis)")
    if has_printer:
        print("✓ Print either the classic JetBot parts or the newer JetNova design.")
        print("  See: docs/designs/JETNOVA.md")
    else:
        print("• No printer? Use any of these:")
        print("  - Foam core / corrugated plastic")
        print("  - Plywood / cardboard + hot glue")
        print("  - LEGO Technic")
        print("  - Plastic container lid as a base plate")
        print("  Goal: motors parallel, camera has clear view, battery sits low.")

    # ---- Eyes ----
    header("5. Eyes (Camera)")
    if has_camera:
        print("✓ Any camera that can give frames to OpenCV/YOLO works.")
        print("  CSI (Pi Cam) is cleaner on Jetson; USB webcam is the easiest start.")
    else:
        print("• Use a laptop webcam first to test the AI demos.")
        print("  Later add a USB webcam or Pi Camera Module 3.")

    # ---- Power ----
    header("6. Power")
    if has_battery:
        print("✓ Keep motor power and brain power conceptually separate.")
        print("  Rule: never power the motors from the Jetson’s 5 V pins.")
    else:
        print("• Two power banks is a perfectly valid start:")
        print("  one for the Jetson, one for the motors + driver.")

    # ---- Assembly order ----
    header("7. Recommended Assembly Order (do this in sequence)")
    steps = [
        "Build or improvise the chassis and mount the two motors + wheels",
        "Add the motor driver and connect motor wires (no brain yet)",
        "Give the driver its own battery and verify motors can spin",
        "Mount the Jetson / Pi and connect the control signals to the driver",
        "Mount and connect the camera",
        "Power the brain, install software, run:  ./demo.sh dashboard",
        "Once phone control works, try:  ./demo.sh follow",
    ]
    for i, s in enumerate(steps, 1):
        print(f"  {i}. {s}")

    # ---- Mental model ----
    header("8. What is happening when a demo runs?")
    print(
        """
  Camera captures image
        ↓
  AI (YOLO etc.) decides what it sees
        ↓
  Software chooses left_speed and right_speed
        ↓
  Motor driver turns those numbers into real current
        ↓
  Motors turn → robot moves
        ↓
  New camera image … (loop)
"""
    )
    print("The web dashboard lets YOU set the speeds directly from your phone.")
    print("Voice and skills are just different ways of choosing those speeds.")

    # ---- Next action ----
    header("9. Your Next Concrete Action")
    if brain == "laptop":
        print("→ On your computer run the vision demos with a webcam first.")
        print("  Get comfortable with YOLO follow / find before building hardware.")
    elif not (has_motors and has_driver):
        print("→ Gather or order: two motors + L298N (or Motor HAT) + any camera.")
        print("  That is the minimum viable mobile robot.")
    else:
        print("→ Assemble chassis + motors + driver, then run:")
        print("     ./demo.sh dashboard")
        print("  If the robot moves from your phone, the whole stack is alive.")

    print("\nDetailed reference:  docs/build/INTERACTIVE_BUILD_GUIDE.md")
    print("Cooler mechanical design:  docs/designs/JETNOVA.md")
    print("\nHappy building!\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
