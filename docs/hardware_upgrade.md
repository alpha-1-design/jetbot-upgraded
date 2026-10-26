# Hardware Upgrade Guide – JetBot 2026

## Recommended Modern Configuration

### Compute
| Option | Performance | Notes | Approx Price |
|--------|-------------|-------|--------------|
| **Jetson Orin Nano Super** | Best value | 67–102 TOPS, ideal for this project | ~$250 |
| Jetson Orin NX 8GB/16GB | Higher | More CUDA cores, better for heavy models | higher |
| Jetson AGX Orin | Overkill | Only if you want max performance | high |

The original Jetson Nano still works for basic demos but is no longer recommended.

### Chassis & Mechanical
The original 3D-printed chassis files in `assets/` still fit most modern kits.

Popular ready-made options:
- Waveshare JetBot (Orin Nano version)
- SparkFun JetBot kits (updated)
- Custom builds using the provided STLs

### Motor Driver Options
1. **Original Adafruit Motor HAT** – still supported (I2C)
2. **Waveshare Motor Driver HAT** – better current handling
3. **Custom** – any I2C or serial motor controller (code is abstracted)

### Camera Recommendations
| Camera | Interface | Recommendation |
|--------|-----------|----------------|
| Raspberry Pi Camera Module 3 | CSI | Best quality + autofocus, official support |
| Arducam IMX219 / IMX477 | CSI | Good alternatives |
| Intel RealSense D435i / D455 | USB | Depth + RGB – excellent for mapping with nvblox |
| ZED 2i / Mini | USB | High quality stereo |

### Optional Upgrades
- **LiDAR**: RPLidar A1M8 / A2M12 or YDLidar – enables proper SLAM
- **IMU**: Built into many RealSense or add BNO085 / BMI160
- **Display**: Small OLED or HDMI screen for status
- **Battery**: Higher capacity 3S/4S LiPo or modern USB-C PD power bank solutions
- **Wheels**: Higher quality rubber tires for better traction

## Bill of Materials (Modern Recommended)

See the updated `docs/bill_of_materials_modern.md` (to be expanded).

## Assembly Notes
Most assembly steps from the original `docs/hardware_setup.md` still apply.  
Main changes:
- Jetson Orin boards have different mounting holes → use updated standoffs or adapter plates.
- Power delivery is more demanding → use a good 5V/20V PD or dedicated power module.
- CSI cameras require the official flex cable and correct device tree overlays.