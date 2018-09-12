import rubiks_cube as cube
import numpy as np


def callback(prev_obs, obs, action, reward, done):
    print("====================== Previous observation ======================")
    print(np.reshape(prev_obs, 54))
    print("======================= Current observation ======================")
    print(np.reshape(obs, 54))
    print("============================= Action =============================")
    print(action)
    print("============================= Reword =============================")
    print(reward)
    print("============================== Done ==============================")
    print(done)
    print("==================================================================")


""" Environment will be scrumble by the move inside test_list """
# test_list = ["ui", "dI", "L", "D", "L", "D", "L", "D", "L", "Di", "Li"]
test_list = [0, 6, 11, 8]

""" Play the game manualy """
env = cube.make()
print(env.action_space)
env.play(callback=callback, scramble=test_list)

""" Each step at the time """
env = cube.make()
num_done = 0
for i_episode in range(200):
    observation = env.reset(test_list)
    for t in range(20):
        action = env.action_space.sample()
        prev_obs = observation
        observation, reward, done = env.step(action)
        isopen = env.render()
        callback(prev_obs, observation, action, reward, done)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print("Reward: ", reward)
            print("Time: ", env._elapsed_seconds)
            num_done += 1
            break
    if isopen == False:
        break
print("Number of finished games: ", num_done)
env.close()
