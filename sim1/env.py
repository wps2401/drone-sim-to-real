import numpy as np
import gymnasium as gym
from gymnasium import spaces
from sim1.physics import DronePhysics

class DroneHoverEnv(gym.Env):
    # Gymnasium environment for a single drone hover task.
    # The agent's goal is to reach and hold z = target_z meters.
    # PPO talks to this class only, it never touches DronePhysics directly.

    def __init__(self):
        super().__init__()
        self.target_z = 10.0
        self.max_steps = 1000
        self.physics = DronePhysics(dt=0.01)

        # Thrust upper bound (20N) gives the agent ~2x hover thrust headroom
        # on a 1kg drone (hover = mass * gravity = 9.81N).
        self.action_space = spaces.Box(
            low=np.array([0.0, -1.0, -1.0, -1.0], dtype=np.float32),
            high=np.array([20.0, 1.0, 1.0, 1.0], dtype=np.float32)
        )

        # Unbounded — position and velocity can grow large during early training
        # before the agent learns to stabilize.
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(13,), dtype=np.float32)

    def reset(self, seed=None, options=None):
        # seed is passed through to the parent so Gymnasium's RNG stays reproducible.
        super().reset(seed=seed)
        self.step_count = 0
        self.physics.state = {
            'x': 0.0, 'y': 0.0, 'z': 0.0,
            'vx': 0.0, 'vy': 0.0, 'vz': 0.0,
            'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
            'p': 0.0, 'q': 0.0, 'r': 0.0
        }
        obs = self._get_obs()
        return obs, {}

    def step(self, action):
        thrust, roll_torque, pitch_torque, yaw_torque = action
        self.physics.step(thrust, roll_torque, pitch_torque, yaw_torque)
        self.step_count += 1

        obs = self._get_obs()

        # Dense reward: zero at target altitude, increasingly negative further away.
        # Dense rewards train faster than sparse (+1 on success) for continuous control.
        reward = -abs(self.physics.state['z'] - self.target_z)

        # terminated = unrecoverable failure (crash). Tells PPO this episode ended badly.
        # truncated = time limit reached. Tells PPO the episode ended cleanly, not by failure.
        terminated = self.physics.state['z'] < 0
        truncated = self.step_count >= self.max_steps

        return obs, reward, terminated, truncated, {}

    def _get_obs(self):
        # Flat array of full 6-DOF state + target altitude.
        # target_z is included so the agent has a reference, without it the agent can't know if z=5 is good or bad.
        s = self.physics.state
        return np.array([
            s['x'], s['y'], s['z'],
            s['vx'], s['vy'], s['vz'],
            s['roll'], s['pitch'], s['yaw'],
            s['p'], s['q'], s['r'],
            self.target_z
        ], dtype=np.float32)