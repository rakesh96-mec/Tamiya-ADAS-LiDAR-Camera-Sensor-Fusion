# Tamiya ADAS – LiDAR & Camera Sensor Fusion

Ongoing ADAS prototype integrating LiDAR, camera, YOLO-based object detection, and NVIDIA Jetson Orin Nano on a Tamiya/Toyota robotic vehicle platform.

## Project Overview

This project investigates multi-sensor perception for an autonomous/assisted robotic vehicle.

The current platform combines:

- NVIDIA Jetson Orin Nano
- Logitech C920 camera
- RPLIDAR A1M8
- Tamiya/Toyota RC vehicle platform
- RC receiver and electronic speed controller (ESC)
- Python, OpenCV and YOLO

The vehicle is currently manually driven while perception and safety functions are being developed. The intended system uses sensor information to detect obstacles and provide an obstacle-aware safety override.

## Current Development

Current work includes:

- Real-time camera-based object detection using YOLO
- LiDAR scanning and visualization
- Camera–LiDAR data association
- Approximate camera–LiDAR projection
- Distance estimation from LiDAR measurements
- Jetson-based hardware and sensor integration
- PWM testing for vehicle control
- GPIO and LiDAR communication tests

Camera–LiDAR calibration and spatial alignment are part of the ongoing development. The current fusion demonstration uses an intentionally uncalibrated approximate projection.

## Repository Contents

| File | Purpose |
|---|---|
| `uncalibrated_camera_lidar_fusion.py` | Camera–LiDAR fusion demonstration with YOLO |
| `rplidar_2d_scan_visualization.py` | Real-time RPLIDAR 2D scan visualization |
| `rplidar_connection_test.py` | RPLIDAR communication and scan test |
| `esc_pwm_test.py` | PWM testing for ESC control |
| `gpio_output_test.py` | GPIO output test |

## System Architecture

```text
Camera ─────────────┐
                    │
                    ▼
              NVIDIA Jetson
                    │
              YOLO + OpenCV
                    │
LiDAR ─────────────┤
                    │
                    ▼
          Multi-Sensor Perception
                    │
                    ▼
          Obstacle-Aware Safety
                 Override
                    │
                    ▼
             RC Vehicle / ESC
```

## Research Direction

The project is being developed as a practical platform for studying:

- Multi-sensor fusion
- Camera–LiDAR perception
- Obstacle detection and distance estimation
- Robotic vehicle safety
- Real-time embedded perception
- Autonomous systems

## Status

**Ongoing**

The current implementation is a development prototype. Sensor calibration, improved fusion, and vehicle-level safety integration are continuing.

## Hardware

- NVIDIA Jetson Orin Nano
- Logitech C920 camera
- RPLIDAR A1M8
- Tamiya/Toyota RC vehicle platform
- RC receiver
- Electronic speed controller (ESC)

## Software

- Python
- OpenCV
- YOLO
- NVIDIA Jetson / CUDA environment
- RPLIDAR Python library

## Project Context

Developed as part of an M.Sc. Mechatronics scientific project with a focus on robotics, computer vision, sensor fusion, and autonomous systems.
