import cube
import numpy as np


def callback(prev_obs, obs, action, reward, done):
    print("====================== Previous observation ======================")
    print(np.reshape(prev_obs, 54))
    print("====================== Current observation ======================")
    print(np.reshape(obs, 54))
    print("====================== Action, Reword and Done ======================")
    print(action, reward, done)


""" Play the game manualy """
env = cube.make()
env.play(callback=callback)

""" Each step at the time """
# env = cube.make()
# env.reset()
# obs, reward, done = env.step("U")
# print(obs, reward, done)
