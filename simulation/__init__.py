"""
Digital twin / simulation support for JetBot Upgraded.

- Pure-Python kinematics twin (runs anywhere, used for tests & offline dev)
- Isaac Sim scripts (run inside Isaac Sim's python.sh)
"""

from .kinematics_twin import KinematicsTwin, TwinConfig

__all__ = ["KinematicsTwin", "TwinConfig"]
