# Rubik-s-Cube
Rubic's cube 2D environment can be used for testing not only **Reinforcement Learning algorithms** but, also for testing **Convolutional Neural Networks** or other **Deep Neural Networks**. This environment is compatible with libraries such as **TensorFlow** and other machine learning libraries. This environment is purposely created to be as close as possible to the [Gym AI library](https://gym.openai.com/) which makes it easy to use for people who are already familiar with this library.

## Basics
The Rubik's Cube environment reacts to an **action** sent by an **agent** (namely, custom machine learning algorithm). After receiving an action, the environment will return back ``observation``, ``reward`` and ``done`` discussed later. The environment interface can be found inside the ``rubiks_cube.py`` class which contains various methods to control the environment.

## Environment Initialization
There are three steps which have to be done to initialize an environment as shows code below. The ``make`` function will return an instance of a Cube class which controls the environment. The environment **must** be **reset** before performing an action on the environment which is provided by the ``reset`` function, otherwise, the environment will not perform an action and it will return an error. The ``reset`` function will ensure that the environment is initialized and the cube is scrambled. This function will also store the time variable that can be used to calculate how long it took to solve the cube. 
```python
import rubiks_cube as cube
env = cube.make()             # get instance of a cube
observation = env.reset()     # reset the environment
```

## Actions
An action is a discrete number between 0 and 11 where each number signifies a move that rotates the cube.

![Alt Text](https://cpb-us-e1.wpmucdn.com/sites.psu.edu/dist/f/25207/files/2015/04/Screen-Shot-2015-04-15-at-9.41.17-PM.png)

Number | Move
------ | ----
0 | U clockwise
1 | U anti-clockwise
2 | D clockwise
3 | D anti-clockwise
4 | L clockwise
5 | L anti-clockwise
6 | R clockwise
7 | R anti-clockwise
8 | F clockwise
9 | F anti-clockwise
10 | B clockwise
11 | B anti-clockwise

## Step function
The agent sends action to the environment by using ``step`` function, which will perform rotation of the cube. The ``step`` function returns `observation`, `reward` and `done`.
```python
observation, reward, done = env.step(action)  # Action is a number between 0 and 11
```

### Observation
The ``observation`` variable is a numpy array of dimensions ( number of faces = **6** ) **x** ( pieces per row = **3** ) **x** ( pieces per column = **3** ) where each element of this array contains a numeric value of the cube's piece color. The piece colour is represented by a discrete number between 0 and 5 as shows table below.

Number | Color
------ | ----
0 | White
1 | Green
2 | Red
3 | Blue
4 | Orange
5 | Yellow

### Reward
A reward variable is a float number which is normalized to be between **-1** and **1**. The reward class is located in the ``reward.py`` file which contains two ways of how reward can be calculated. The first way is by using the ``calculate_reward_pieces_color()`` method which returns reward based on the cube's wall colours by taking a percentage of the correct colours per each wall. The other way is to use the ``calculate_reward_pieces_position()`` method which checks if every piece is in a correct position. These two methods can be swapped by commenting and uncommenting the following lines.
```python
return calculate_reward_pieces_color()
# return calculate_reward_pieces_position()
```

### Done
The ``done`` variable is represented by the boolean data type where **True** indicates that the cube is solved and **False** indicates that the cube is **not** solved.  

## Play the game
The environment allows developer to run it manually by using keybord which will perform a cube move.
```python
import rubiks_cube as cube
env = cube.make()
env.play()
```
