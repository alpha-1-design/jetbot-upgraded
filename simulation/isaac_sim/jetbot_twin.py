#!/usr/bin/env python3
"""
Isaac Sim digital twin for JetBot / JetNova.

Run INSIDE Isaac Sim:

  ./python.sh path/to/jetbot_twin.py
  ./python.sh path/to/jetbot_twin.py --headless --test

Uses the official NVIDIA Jetbot USD asset + DifferentialController.
Control API intentionally matches jetbot.modern_robot.Robot so behaviors
can be shared between real hardware and simulation.
"""

from __future__ import annotations

import argparse
import sys
import time


def parse_args():
    p = argparse.ArgumentParser(description="JetBot Isaac Sim digital twin")
    p.add_argument("--headless", action="store_true", help="Run without GUI")
    p.add_argument("--test", action="store_true", help="Short automated motion test then exit")
    p.add_argument("--duration", type=float, default=12.0, help="Seconds to run in demo mode")
    p.add_argument("--linear", type=float, default=0.25, help="Linear speed m/s for demo")
    p.add_argument("--angular", type=float, default=0.6, help="Angular speed rad/s for demo")
    return p.parse_args()


def main():
    args = parse_args()

    # Isaac Sim bootstrap – must happen before most omni/isaac imports
    from isaacsim import SimulationApp
    simulation_app = SimulationApp({"headless": args.headless})

    import numpy as np
    import isaacsim.core.experimental.utils.app as app_utils
    from isaacsim.core.experimental.objects import DomeLight
    from isaacsim.core.simulation_manager import SimulationManager
    from isaacsim.robot.experimental.wheeled_robots.controllers import DifferentialController
    from isaacsim.robot.experimental.wheeled_robots.robots import WheeledRobot
    from isaacsim.storage.native import get_assets_root_path
    import isaacsim.core.experimental.utils.stage as stage_utils

    # ----- Scene -----
    stage_utils.create_new_stage()
    SimulationManager.set_physics_sim_device(1.0 / 60.0)
    DomeLight(paths="/World/DomeLight", intensities=[1000.0])

    assets_root = get_assets_root_path()
    if assets_root is None:
        print("ERROR: Could not find Isaac Sim assets root. Is Isaac Sim installed correctly?")
        simulation_app.close()
        sys.exit(1)

    # Official Jetbot asset (ships with Isaac Sim)
    jetbot_usd = assets_root + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
    # Fallback older path used in some versions
    # jetbot_usd = assets_root + "/Isaac/Robots/Jetbot/jetbot.usd"

    print(f"Loading Jetbot USD: {jetbot_usd}")

    robot = WheeledRobot(
        paths="/World/Jetbot",
        wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
        usd_path=jetbot_usd,
        positions=np.array([[0.0, 0.0, 0.05]]),
    )

    # Classic JetBot geometry (matches our TwinConfig.classic / RobotConfig.classic)
    controller = DifferentialController(
        wheel_radius=0.0325,
        wheel_base=0.1125,
    )

    print("JetBot digital twin ready.")
    print("  DifferentialController: wheel_radius=0.0325 m, wheel_base=0.1125 m")

    # ----- Control helpers (Robot-like API) -----
    def apply_twist(linear_m_s: float, angular_rad_s: float):
        """Send body twist; controller turns it into wheel velocities."""
        actions = controller.forward(np.array([linear_m_s, angular_rad_s]))
        robot.apply_wheel_actions(actions)

    def stop():
        apply_twist(0.0, 0.0)

    # ----- Main loop -----
    step = 0
    max_steps = int(args.duration * 60) if not args.test else 90
    phase = 0
    phase_steps = 0

    # Simple demo state machine: forward → turn → forward → stop
    demo_phases = [
        (args.linear, 0.0, 90),       # forward
        (0.05, args.angular, 60),    # turn left
        (args.linear, 0.0, 90),       # forward again
        (0.0, 0.0, 30),              # stop
    ]

    while simulation_app.is_running():
        simulation_app.update()
        if not app_utils.is_playing():
            continue

        step += 1
        phase_steps += 1

        if phase < len(demo_phases):
            lin, ang, hold = demo_phases[phase]
            apply_twist(lin, ang)
            if phase_steps >= hold:
                phase += 1
                phase_steps = 0
                print(f"  phase → {phase}")
        else:
            stop()

        if args.test and step >= max_steps:
            print("Test run finished OK.")
            break
        if not args.test and step >= max_steps:
            break

    stop()
    simulation_app.close()
    print("Isaac Sim twin closed.")


if __name__ == "__main__":
    main()
