"""
Pure-Python differential-drive digital twin.

Runs on any machine (no Isaac Sim required).
Used for:
  - unit tests
  - offline development of behaviors
  - CI
  - students without a GPU workstation

API mirrors jetbot.modern_robot.Robot as closely as possible.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass
from typing import Optional, Tuple, List


@dataclass
class TwinConfig:
    """Geometry and limits – aligned with RobotConfig where possible."""
    name: str = "classic"
    wheel_radius_m: float = 0.0325          # 65 mm diameter
    wheel_base_m: float = 0.120             # classic JetBot approx
    max_linear_speed_m_s: float = 0.4
    max_angular_speed_rad_s: float = 2.0
    # How normalized motor commands [-1, 1] map to wheel angular velocity
    max_wheel_omega_rad_s: float = 15.0     # roughly matches small geared motors

    @classmethod
    def classic(cls) -> "TwinConfig":
        return cls(name="classic", wheel_radius_m=0.0325, wheel_base_m=0.120)

    @classmethod
    def jetnova(cls) -> "TwinConfig":
        return cls(
            name="jetnova",
            wheel_radius_m=0.0375,   # 75 mm wheels
            wheel_base_m=0.165,
            max_linear_speed_m_s=0.5,
            max_angular_speed_rad_s=2.2,
        )


class KinematicsTwin:
    """
    Simple 2D differential-drive twin.

    State: x, y (metres), theta (radians, 0 = +x)
    Control: left/right normalized motor commands in [-1, 1]  (same as Robot)

    Usage:
        twin = KinematicsTwin(TwinConfig.jetnova())
        twin.set_motors(0.3, 0.3)
        twin.step(0.05)          # advance 50 ms
        print(twin.x, twin.y, twin.theta)
    """

    def __init__(self, config: Optional[TwinConfig] = None):
        self.config = config or TwinConfig.classic()
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self._left_cmd = 0.0
        self._right_cmd = 0.0
        self._time = 0.0
        self.trajectory: List[Tuple[float, float, float, float]] = []  # t, x, y, theta

    # ----- API compatible with modern_robot.Robot -----

    def set_motors(self, left_speed: float, right_speed: float):
        self._left_cmd = max(-1.0, min(1.0, float(left_speed)))
        self._right_cmd = max(-1.0, min(1.0, float(right_speed)))

    def forward(self, speed: float = 0.3):
        self.set_motors(speed, speed)

    def backward(self, speed: float = 0.3):
        self.set_motors(-speed, -speed)

    def left(self, speed: float = 0.3):
        self.set_motors(-speed, speed)

    def right(self, speed: float = 0.3):
        self.set_motors(speed, -speed)

    def stop(self):
        self.set_motors(0.0, 0.0)

    # ----- Simulation step -----

    def step(self, dt: float):
        """Integrate kinematics for dt seconds."""
        if dt <= 0:
            return

        # Wheel angular velocities
        omega_l = self._left_cmd * self.config.max_wheel_omega_rad_s
        omega_r = self._right_cmd * self.config.max_wheel_omega_rad_s

        # Linear velocities of each wheel
        v_l = omega_l * self.config.wheel_radius_m
        v_r = omega_r * self.config.wheel_radius_m

        # Body twist
        v = 0.5 * (v_l + v_r)
        omega = (v_r - v_l) / self.config.wheel_base_m

        # Clamp for realism
        v = max(-self.config.max_linear_speed_m_s,
                min(self.config.max_linear_speed_m_s, v))
        omega = max(-self.config.max_angular_speed_rad_s,
                    min(self.config.max_angular_speed_rad_s, omega))

        # Unicycle integration
        if abs(omega) < 1e-6:
            self.x += v * math.cos(self.theta) * dt
            self.y += v * math.sin(self.theta) * dt
        else:
            # Exact integration for constant v, omega
            self.x += (v / omega) * (math.sin(self.theta + omega * dt) - math.sin(self.theta))
            self.y += (v / omega) * (-math.cos(self.theta + omega * dt) + math.cos(self.theta))
            self.theta += omega * dt

        # Normalize theta
        self.theta = (self.theta + math.pi) % (2 * math.pi) - math.pi
        self._time += dt
        self.trajectory.append((self._time, self.x, self.y, self.theta))

    def run(self, duration: float, dt: float = 0.02):
        """Step for a fixed duration."""
        steps = int(duration / dt)
        for _ in range(steps):
            self.step(dt)

    def reset(self, x: float = 0.0, y: float = 0.0, theta: float = 0.0):
        self.x, self.y, self.theta = x, y, theta
        self._left_cmd = self._right_cmd = 0.0
        self._time = 0.0
        self.trajectory.clear()

    def pose(self) -> Tuple[float, float, float]:
        return self.x, self.y, self.theta

    def __repr__(self) -> str:
        return (f"KinematicsTwin(name={self.config.name}, "
                f"x={self.x:.3f}, y={self.y:.3f}, θ={math.degrees(self.theta):.1f}°)")
