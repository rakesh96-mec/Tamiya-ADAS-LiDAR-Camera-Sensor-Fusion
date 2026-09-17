import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from rplidar import RPLidar

PORT = '/dev/ttyUSB0'

# IMPORTANT: Use the baud rate that worked for you
lidar = RPLidar(PORT, baudrate=460800)

fig, ax = plt.subplots(figsize=(8,8))

scatter = ax.scatter([], [], s=8)

ax.set_xlim(-5000, 5000)
ax.set_ylim(-5000, 5000)

ax.set_xlabel("X (mm)")
ax.set_ylabel("Y (mm)")
ax.set_title("Live RPLIDAR Scan")

ax.grid(True)
ax.set_aspect('equal')

scan_generator = lidar.iter_scans()

def update(frame):

    scan = next(scan_generator)

    x = []
    y = []

    for quality, angle, distance in scan:

        if distance == 0:
            continue

        angle_rad = math.radians(angle)

        x.append(distance * math.cos(angle_rad))
        y.append(distance * math.sin(angle_rad))

    scatter.set_offsets(list(zip(x, y)))

    return scatter,

# ani = FuncAnimation(fig, update, interval=40)

# plt.show()
import os

if os.environ.get("DISPLAY"):
    ani = FuncAnimation(fig, update, interval=40)
    plt.show()
else:
    print("No graphical display available.")

lidar.stop()
lidar.disconnect()
