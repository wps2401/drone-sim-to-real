# camera.py
# Software model of a camera
# Contains a set height width resolution and an image

import numpy as np

class CameraSensor:
    def __init__(self, height, width): # init stores height and width since this is a set resolution that doesn't change frame to frame
        self.height = height
        self.width = width

    def read(self, image):
        return image