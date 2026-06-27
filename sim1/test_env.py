# Smoke test for DroneHoverEnv.
# Verifies the Gymnasium contract: reset returns a valid obs,
# step returns obs/reward/terminated/truncated without crashing.
# Uses random actions. Not learning, just checking the plumbing.

from sim1.env import DroneHoverEnv

env = DroneHoverEnv()
obs, info = env.reset()
print("Initial obs:", obs)

for i in range(5):
    # action_space.sample() draws a random action within the defined bounds.
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"Step {i+1}: z={obs[2]:.3f}, reward={reward:.3f}, terminated={terminated}, truncated={truncated}")

print("Smoke test passed.")