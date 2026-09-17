from rplidar import RPLidar

PORT = '/dev/ttyUSB0'

lidar = RPLidar(PORT, baudrate = 460800)

for scan in lidar.iter_scans():
    print(scan)
    
    