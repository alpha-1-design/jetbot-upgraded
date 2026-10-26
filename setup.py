from setuptools import setup, find_packages

setup(
    name='jetbot',
    version='0.5.0-upgraded',
    description='Upgraded open-source educational AI robot based on NVIDIA Jetson (Orin / modern boards)',
    long_description=open('README.md').read() if True else '',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        # Core
        'numpy',
        'Pillow',
        'traitlets',
        # Camera / vision (modern)
        'opencv-python',
        # Optional motor / display (original still supported)
        'Adafruit-MotorHat; python_version < "3.12"',
        'Adafruit-SSD1306',
        'sparkfun-qwiic',
        # Modern AI helpers (install separately on Jetson for TensorRT / CUDA)
        # 'ultralytics',   # YOLOv8 – install via pip when needed
        # 'onnxruntime-gpu',
    ],
    extras_require={
        'yolo': ['ultralytics'],
        'ros': [],  # handled via ROS packages
    },
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Education',
    ],
)
