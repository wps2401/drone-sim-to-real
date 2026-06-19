# gps.py
# Software model of a Geographic Positioning System (GPS)
# Contains position (x, y, z) and velocity (vx, vy, vz)

import numpy as np

class GPSSensor:
    def __init__(self): # Right now, init does nothing. IMU has no current state to set up, but will add things like position error later.
        pass

    def read(self, true_position, true_velocity):
        return true_position, true_velocity