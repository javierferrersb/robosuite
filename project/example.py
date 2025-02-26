import numpy as np
import robosuite as suite

# create environment instance
env = suite.make(
    env_name="Door",  # try with other tasks like "Stack" and "Door"
    robots="Sawyer",  # try with other robots like "Sawyer" and "Jaco"
    has_renderer=True,
    has_offscreen_renderer=False,
    use_camera_obs=False,
)

# reset the environment
env.reset()

for i in range(1000):
    action = np.random.randn(*env.action_spec[0].shape) * 0.1
    # take action in the environment
    obs, reward, done, info = env.step(action)
    env.render()  # render on display

# close the environment
env.close()
