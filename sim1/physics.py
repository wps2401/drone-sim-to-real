# physics.py

import numpy as np

class DronePhysics:

    def __init__(self, dt=0.01):
        self.dt = dt
        self.state = {
            'x': 0.0,
            'y': 0.0,
            'z': 0.0,
            'vx': 0.0,  
            'vy': 0.0,
            'vz': 0.0,
            'roll': 0.0,
            'pitch': 0.0,
            'yaw': 0.0,
            'p': 0.0,       #roll rate
            'q': 0.0,       #pitch rate
            'r': 0.0        #yaw rate
        }

    def step(self, thrust, roll_torque, pitch_torque, yaw_torque):
        inertia = 0.01
        self.state['p'] += (roll_torque / inertia) * self.dt
        self.state['q'] += (pitch_torque / inertia) * self.dt
        self.state['r'] += (yaw_torque / inertia) * self.dt
        return self.state
