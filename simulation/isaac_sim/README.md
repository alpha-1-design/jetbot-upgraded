# Isaac Sim scripts

These scripts are meant to be launched with Isaac Sim’s own Python:

```bash
./python.sh jetbot_twin.py
./python.sh jetbot_twin.py --headless --test
```

They will not run under the system `python3` unless Isaac Sim’s environment is active.

For everyday testing without Isaac Sim, use:

```bash
python3 -m simulation.tests.test_kinematics_twin
# or
python3 simulation/tests/test_kinematics_twin.py
```
