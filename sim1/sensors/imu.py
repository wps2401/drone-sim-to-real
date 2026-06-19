# imu.py
# Software model of an Inertial Measurement Unit (IMU)
# Contains accelerometer (ax, ay, az) and gyroscope (gx, gy, gz) models
# Currently operates in pass-through mode (no noise)
# Noise models (bias, drift, random jitter) will be added in a later phase

import numpy as np

class IMUSensor:
    def __init__(self): # Right now, init does nothing. IMU has no current state to set up, but will add things like drift and bias later.
        pass

    def read(self, true_accel, true_gyro):
        return true_accel, true_gyro