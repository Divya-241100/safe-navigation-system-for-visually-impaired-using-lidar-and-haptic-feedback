from lidar import get_distance
from alerts import alert_system
import time

THRESHOLD = 100  # cm

print("Safe Navigation System Started on Raspberry Pi...")

while True:
    distance = get_distance()
    print("Distance:", distance, "cm")

    if distance <= THRESHOLD:
        alert_system(distance)
    else:
        print("Path is clear")

    time.sleep(0.2)
