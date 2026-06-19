# barometer.py
# Software model of a barometer
# Contains altitude

import numpy as np

class BarometerSensor:
    def __init__(self): # Right now, init does nothing. barometer has no current state to set up
        pass

    def read(self, true_altitude):
        return true_altitude