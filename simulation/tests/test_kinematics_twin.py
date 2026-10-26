#!/usr/bin/env python3
"""Unit tests for the pure-Python digital twin (no Isaac Sim required)."""

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from simulation.kinematics_twin import KinematicsTwin, TwinConfig


def approx(a, b, tol=1e-3):
    return abs(a - b) < tol


def test_forward_motion():
    twin = KinematicsTwin(TwinConfig.classic())
    twin.forward(0.5)
    twin.run(1.0, dt=0.02)
    x, y, th = twin.pose()
    assert x > 0.05, f"Expected forward progress, got x={x}"
    assert approx(y, 0.0, 0.02), f"Expected little lateral drift, y={y}"
    assert approx(th, 0.0, 0.1), f"Expected heading ~0, th={th}"
    print("  ✓ forward_motion")


def test_spin_in_place():
    twin = KinematicsTwin(TwinConfig.classic())
    twin.left(0.5)
    twin.run(1.0, dt=0.02)
    x, y, th = twin.pose()
    # Should mostly rotate, little translation
    assert abs(x) < 0.05 and abs(y) < 0.05, f"Spin drifted too much: {x},{y}"
    assert abs(th) > 0.3, f"Expected noticeable rotation, th={th}"
    print("  ✓ spin_in_place")


def test_stop():
    twin = KinematicsTwin()
    twin.forward(0.4)
    twin.run(0.5)
    twin.stop()
    x1, y1, _ = twin.pose()
    twin.run(0.5)
    x2, y2, _ = twin.pose()
    assert approx(x1, x2) and approx(y1, y2)
    print("  ✓ stop")


def test_jetnova_geometry_differs():
    classic = KinematicsTwin(TwinConfig.classic())
    jetnova = KinematicsTwin(TwinConfig.jetnova())
    classic.left(0.5)
    jetnova.left(0.5)
    classic.run(1.0)
    jetnova.run(1.0)
    # Different wheelbase → different yaw rate for same wheel commands
    assert abs(classic.theta - jetnova.theta) > 0.05
    print("  ✓ jetnova_geometry_differs")


def test_api_surface():
    twin = KinematicsTwin()
    for method in ("forward", "backward", "left", "right", "stop", "set_motors"):
        assert hasattr(twin, method)
    twin.set_motors(0.2, -0.2)
    twin.step(0.05)
    print("  ✓ api_surface")


def test_trajectory_recorded():
    twin = KinematicsTwin()
    twin.forward(0.3)
    twin.run(0.5, dt=0.05)
    assert len(twin.trajectory) == 10
    print("  ✓ trajectory_recorded")


if __name__ == "__main__":
    print("Running kinematics twin tests...")
    test_forward_motion()
    test_spin_in_place()
    test_stop()
    test_jetnova_geometry_differs()
    test_api_surface()
    test_trajectory_recorded()
    print("All tests passed.")
