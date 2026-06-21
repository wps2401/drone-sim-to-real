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
        mass = 1.0
        gravity = 9.81
        ax = (thrust / mass) * np.sin(self.state['pitch'])
        ay = (thrust / mass) * -np.sin(self.state['roll'])
        az = (thrust / mass) * np.cos(self.state['roll']) * np.cos(self.state['pitch']) - gravity
        
        self.state['p'] += (roll_torque / inertia) * self.dt
        self.state['q'] += (pitch_torque / inertia) * self.dt
        self.state['r'] += (yaw_torque / inertia) * self.dt
        self.state['roll'] += self.state['p'] * self.dt
        self.state['pitch'] += self.state['q'] * self.dt
        self.state['yaw'] += self.state['r'] * self.dt

        self.state['vx'] += ax * self.dt
        self.state['vy'] += ay * self.dt
        self.state['vz'] += az * self.dt
        self.state['x'] += self.state['vx'] * self.dt
        self.state['y'] += self.state['vy'] * self.dt
        self.state['z'] += self.state['vz'] * self.dt

        return self.state
