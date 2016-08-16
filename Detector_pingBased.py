import Ping_Driver


#1 meter
distance_at_nobody_there = 100


def detect_person():
    if Ping_Driver.distance() < (0.7*distance_at_nobody_there):
        return True
    else:
        return False

