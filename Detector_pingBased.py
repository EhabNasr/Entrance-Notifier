import Ping_Driver
import time

#1 meter
distance_at_nobody_there = 100


def detect_person():
#    time.sleep(0.2)
    if Ping_Driver.distance() < (0.5*distance_at_nobody_there):
        return True
    else:
        return False

