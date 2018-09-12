import random
import numpy as np
import rendering
import play as game
from space import Moves
from space import Discrete
from space import Action
import time
from reward import Reward

""" Rubik's Cube Environment """


class Cube:
    def __init__(self):
        self.num_faces = 6
        self.num_pieces_per_face = 9  # size of cube => 9 for 3x3 cube
        self.num_pieces_per_row = int(np.sqrt(self.num_pieces_per_face))
        self.num_pieces_per_col = self.num_pieces_per_row
        self.position_array_row_size = 2
        self.piece_size = 50
        self.cube_colors = np.full(
            (self.num_faces, self.num_pieces_per_row, self.num_pieces_per_col), 0)
        self.action_space = Discrete(11)  # 11 is the number of possible moves
        self.action_move = Action(self)       # Actions that cube can perform
        self.action_reward = Reward(self)
        self.view = None
        self.steps_beyond_done = False
        self.episode_started_at = None

    @property
    def _elapsed_seconds(self):
        """ Get time since episode started
            return: float
                Time in seconds
        """
        return time.time() - self.episode_started_at

    def step(self, action):
        """ Perform an Action on the environment
            :param action: int
                Discrete number between 0 and 11 (Avalaible moves to rotate cube)
        """
        assert self.episode_started_at is not None, "Cannot call env.step() before calling reset()"
        assert self.action_space.contains(
            action) is not None, "%r is invalid action" % action
        self.action_move.rotate_cube(self.cube_colors, Moves(action))
        if self.action_move.is_solved(self.cube_colors):
            reward = 1.0
            done = True
        else:
            reward = self.action_reward.calculate_reward()
            done = False
        return self.cube_colors, reward, done

    def reset(self, list_moves=None):
        """ Reset environment
            :param list_moves: Array List of Strings, Integers, or None
                Each element is a move that will rotate the cube.
                The elements of the list can be either numeric
                representation of the move (values between 0 and 11),
                or string values (U, Ui, D, Di, L, Li, R, Ri, F, Fi, B, Bi)
                which are case insensitive and can be either uppercase, lower case or mixed.
                If the list_moves is None, then the cube will be scrumbled into super flip
                configuration.
            return: numpy array
                initial observation
        """
        self.action_move.init_colors(self.cube_colors)
        if list_moves == None:
            self.action_move.super_flip_configuration(self.cube_colors)
        else:
            self.action_move.scramble_cube_from_list(
                self.cube_colors, list_moves)
        self.steps_beyond_done = True
        self.episode_started_at = time.time()
        return self.cube_colors

    def render(self):
        """ Render enviroment on the screen
            return: bool
                False if user closed window, otherwise return True
        """
        if self.view == None:
            self.view = rendering.View()
            return self.view.render(self.cube_colors)
        else:
            return self.view.render(self.cube_colors)

    def close(self):
        """ Close the rendering window """
        self.view.close()

    def play(self, fps=30, callback=None, scramble=None):
        """ Play the game manually """
        game.play(self, fps=fps, callback=callback, scramble=scramble)


def make():
    """ Get an instance of the Cube environment """
    return Cube()
