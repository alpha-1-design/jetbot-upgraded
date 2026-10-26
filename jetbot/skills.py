"""
Simple Skills / Behaviors system.

Indie goal: make it easy to compose and share cool robot behaviors
without rewriting motor code every time.
"""

import time
from typing import Callable, Optional
from .modern_robot import Robot
from .config import get_config


class Skill:
    """Base skill. Override `run` or pass a function."""

    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

    def run(self, robot: Robot, **kwargs):
        raise NotImplementedError


class TimedMove(Skill):
    def __init__(self, left: float, right: float, duration: float, name: str = "timed_move"):
        super().__init__(name)
        self.left = left
        self.right = right
        self.duration = duration

    def run(self, robot: Robot, **kwargs):
        robot.set_motors(self.left, self.right)
        time.sleep(self.duration)
        robot.stop()


class Spin(Skill):
    def __init__(self, duration: float = 2.0, speed: float = 0.35):
        super().__init__("spin", "Spin in place")
        self.duration = duration
        self.speed = speed

    def run(self, robot: Robot, **kwargs):
        robot.left(self.speed)
        time.sleep(self.duration)
        robot.stop()


class ForwardBurst(Skill):
    def __init__(self, duration: float = 1.0, speed: float = 0.3):
        super().__init__("forward_burst")
        self.duration = duration
        self.speed = speed

    def run(self, robot: Robot, **kwargs):
        robot.forward(self.speed)
        time.sleep(self.duration)
        robot.stop()


class LookAround(Skill):
    """Small left/right glances – makes the robot feel alive."""

    def __init__(self):
        super().__init__("look", "Glance left and right")

    def run(self, robot: Robot, **kwargs):
        robot.left(0.3)
        time.sleep(0.4)
        robot.stop()
        time.sleep(0.2)
        robot.right(0.3)
        time.sleep(0.8)
        robot.stop()
        time.sleep(0.2)
        robot.left(0.3)
        time.sleep(0.4)
        robot.stop()


# Registry so demos / voice can call skills by name
SKILLS = {
    "spin": Spin(),
    "forward": ForwardBurst(),
    "look": LookAround(),
}


def run_skill(name: str, robot: Optional[Robot] = None, **kwargs):
    if robot is None:
        robot = Robot()
    skill = SKILLS.get(name)
    if skill is None:
        raise ValueError(f"Unknown skill '{name}'. Available: {list(SKILLS.keys())}")
    print(f"[Skill] Running '{name}'")
    skill.run(robot, **kwargs)
