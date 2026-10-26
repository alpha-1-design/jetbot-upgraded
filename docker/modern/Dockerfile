# Modern JetBot base image for JetPack 6.x / L4T R36+
# Target: Jetson Orin Nano Super / Orin NX / AGX Orin

ARG BASE_IMAGE=nvcr.io/nvidia/l4t-jetpack:r36.4.0
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash

# Basic tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    vim \
    cmake \
    build-essential \
    python3-pip \
    python3-dev \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Python packages (core)
RUN pip3 install --upgrade pip && \
    pip3 install \
    numpy \
    Pillow \
    traitlets \
    jupyterlab \
    ipywidgets \
    opencv-python \
    && rm -rf /root/.cache/pip

# Optional: Adafruit / display support (may need platform-specific fixes)
RUN pip3 install Adafruit-SSD1306 sparkfun-qwiic || true

# Workspace
WORKDIR /workspace
COPY . /workspace/jetbot

# Install the package
RUN cd /workspace/jetbot && pip3 install -e .

# Default command
CMD ["bash"]
