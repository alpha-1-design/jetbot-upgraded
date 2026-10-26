# JetBot Upgraded package
# Keep heavy imports lazy so demos can use modern_robot without OpenCV etc.

__version__ = "0.5.0-upgraded"

# Lightweight modern API (preferred for new demos)
from .modern_robot import Robot as ModernRobot

# Legacy names – imported only when available
try:
    from .robot import Robot
except Exception:
    Robot = ModernRobot

try:
    from .motor import Motor
except Exception:
    Motor = None

try:
    from .image import bgr8_to_jpeg
except Exception:
    bgr8_to_jpeg = None

try:
    from .heartbeat import Heartbeat
except Exception:
    Heartbeat = None

# Camera and object detection are intentionally not imported at top level
# so that simple motor demos work even without OpenCV installed.
