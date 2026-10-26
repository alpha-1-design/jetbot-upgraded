"""
Robot configuration system – no longer locked to one chassis design.

Supports:
- Classic JetBot
- JetNova (new cooler design)
- Fully custom geometries and drivers
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class RobotConfig:
    name: str = "classic"
    # Geometry (used later for odometry / simulation)
    wheel_diameter_mm: float = 65.0
    wheel_base_mm: float = 120.0          # distance between left/right wheel centers
    # Motion
    max_speed: float = 0.4                # normalized
    turn_multiplier: float = 1.0
    # Hardware
    motor_driver: str = "adafruit"        # adafruit | waveshare | sparkfun | dummy
    i2c_bus: int = 1
    left_motor_channel: int = 1
    right_motor_channel: int = 2
    left_alpha: float = 1.0               # trim
    right_alpha: float = 1.0
    # Features
    has_pan_tilt: bool = False
    has_lidar: bool = False
    has_depth_camera: bool = False
    has_status_leds: bool = False
    # Extra free-form data
    extras: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def classic(cls) -> "RobotConfig":
        """Original NVIDIA JetBot geometry + defaults."""
        return cls(
            name="classic",
            wheel_diameter_mm=65.0,
            wheel_base_mm=120.0,
            max_speed=0.35,
            motor_driver="adafruit",
            has_pan_tilt=False,
        )

    @classmethod
    def jetnova(cls) -> "RobotConfig":
        """New cooler modular design defaults."""
        return cls(
            name="jetnova",
            wheel_diameter_mm=75.0,
            wheel_base_mm=165.0,
            max_speed=0.45,
            turn_multiplier=1.1,
            motor_driver="adafruit",      # still works; waveshare also common
            has_pan_tilt=True,
            has_status_leds=True,
            extras={
                "recommended_camera": "pi_cam_3_or_realsense",
                "top_deck": True,
                "battery_bay": "enclosed",
            },
        )

    @classmethod
    def dummy(cls) -> "RobotConfig":
        """No hardware – perfect for development and CI."""
        return cls(
            name="dummy",
            motor_driver="dummy",
            max_speed=0.5,
        )


# Global active config (demos can override)
_active_config: Optional[RobotConfig] = None


def get_config() -> RobotConfig:
    global _active_config
    if _active_config is None:
        _active_config = RobotConfig.classic()
    return _active_config


def set_config(cfg: RobotConfig):
    global _active_config
    _active_config = cfg
