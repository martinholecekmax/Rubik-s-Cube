# Rubik-s-Cube
Rubic's cube 2D environment can be used for testing not only **reinforcement learning algorithms** but, also for testing **convolutional neural networks** or other **deep neural networks**. This environment is compatible with libraries such as **TensorFlow** and other machine learning libraries.

## Basics
The Rubik's Cube environment reacts to an **action** sent by an **agent** (namely, custom machine learning algorithm). After receiving an action, the environment will return back ``observation`` and ``reward`` discussed later. The environment interface can be found inside the ``rubiks_cube.py`` class which contains various methods to control the environment.

## Play the game
The environment allows developer to run it manually by using keybord which will perform a cube move.
```python
import rubiks_cube as cube
env = cube.make()
env.play()
```
