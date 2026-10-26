"""
Modern Robot abstraction for JetBot Upgraded / JetNova.

- Not locked to one chassis
- Config-driven (classic, JetNova, or custom)
- Safe defaults + dummy mode for development
"""

import atexit
from typing import Optional

from .config import RobotConfig, get_config, set_config


class ModernMotor:
    """Simple motor wrapper. value is in range [-1.0, 1.0]"""

    def __init__(self, set_speed_fn, alpha=1.0):
        self._set_speed = set_speed_fn
        self.alpha = float(alpha)
        self._value = 0.0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, speed):
        speed = max(-1.0, min(1.0, float(speed))) * self.alpha
        self._value = speed
        self._set_speed(speed)


class Robot:
    """
    High-level differential drive robot.

    Examples:
        robot = Robot()                          # uses active / classic config
        robot = Robot(config=RobotConfig.jetnova())
        robot = Robot(config=RobotConfig.dummy())
    """

    def __init__(self, config: Optional[RobotConfig] = None):
        if config is not None:
            set_config(config)
        self.config = get_config()
        self.left_motor: Optional[ModernMotor] = None
        self.right_motor: Optional[ModernMotor] = None
        self._driver = None
        self._init_motors()
        atexit.register(self.stop)
        print(f"[Robot] Profile: {self.config.name}  |  driver={self.config.motor_driver}")

    def _init_motors(self):
        driver = self.config.motor_driver.lower()

        if driver == "dummy":
            self._init_dummy()
            return

        if driver in ("adafruit", "auto"):
            if self._try_adafruit():
                return

        # Future: waveshare, sparkfun, serial ESCs, etc.
        print(f"[Robot] Driver '{driver}' not available – falling back to dummy")
        self._init_dummy()

    def _try_adafruit(self) -> bool:
        try:
            from Adafruit_MotorHAT import Adafruit_MotorHAT
            self._driver = Adafruit_MotorHAT(i2c_bus=self.config.i2c_bus)
            left = self._driver.getMotor(self.config.left_motor_channel)
            right = self._driver.getMotor(self.config.right_motor_channel)

            def make_setter(motor):
                def set_speed(speed):
                    motor.setSpeed(int(abs(speed) * 255))
                    if speed > 0.02:
                        motor.run(Adafruit_MotorHAT.FORWARD)
                    elif speed < -0.02:
                        motor.run(Adafruit_MotorHAT.BACKWARD)
                    else:
                        motor.run(Adafruit_MotorHAT.RELEASE)
                return set_speed

            self.left_motor = ModernMotor(make_setter(left), alpha=self.config.left_alpha)
            self.right_motor = ModernMotor(make_setter(right), alpha=self.config.right_alpha)
            print("[Robot] Adafruit Motor HAT ready")
            return True
        except Exception as e:
            print(f"[Robot] Adafruit not available ({e})")
            return False

    def _init_dummy(self):
        self.left_motor = ModernMotor(lambda s: None)
        self.right_motor = ModernMotor(lambda s: None)
        print("[Robot] Dummy motors (safe for development)")

    # -------- High-level movement --------

    def set_motors(self, left_speed: float, right_speed: float):
        max_s = self.config.max_speed
        self.left_motor.value = max(-max_s, min(max_s, left_speed))
        self.right_motor.value = max(-max_s, min(max_s, right_speed))

    def forward(self, speed: float = 0.3):
        self.set_motors(speed, speed)

    def backward(self, speed: float = 0.3):
        self.set_motors(-speed, -speed)

    def left(self, speed: float = 0.3):
        self.set_motors(-speed * self.config.turn_multiplier,
                        speed * self.config.turn_multiplier)

    def right(self, speed: float = 0.3):
        self.set_motors(speed * self.config.turn_multiplier,
                        -speed * self.config.turn_multiplier)

    def stop(self):
        self.set_motors(0.0, 0.0)

    def move(self, left: float, right: float, duration: Optional[float] = None):
        self.set_motors(left, right)
        if duration is not None:
            import time
            time.sleep(duration)
            self.stop()
