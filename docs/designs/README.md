# Robot Designs

The software is **not locked** to a single chassis.

## Available Profiles

| Profile   | Description                              | Config call                  |
|-----------|------------------------------------------|------------------------------|
| Classic   | Original NVIDIA JetBot geometry          | `RobotConfig.classic()`      |
| **JetNova** | New cooler modular design (recommended) | `RobotConfig.jetnova()`    |
| Dummy     | No hardware – for development            | `RobotConfig.dummy()`        |
| Custom    | Your own numbers                         | `RobotConfig(...)`           |

## JetNova (the cooler one)

See **[JETNOVA.md](JETNOVA.md)** for the full design brief, BOM, print list, and goals.

JetNova adds:
- Modern sculpted look
- Enclosed battery bay
- Modular top deck (LiDAR / RealSense)
- Optional pan-tilt camera head
- Status light bar
- Better cable management
- Orin Nano Super / Orin NX ready

Classic JetBot hardware continues to work with zero changes.
