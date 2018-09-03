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
        # size of cube => 9 for 3x3 cube
        self.num_pieces_per_face = 9
        self.num_pieces_per_row = int(np.sqrt(self.num_pieces_per_face))
        self.num_pieces_per_col = self.num_pieces_per_row
        self.cube_colors = np.full(
            (self.num_faces, self.num_pieces_per_row, self.num_pieces_per_col), 0)
        self.position_array_row_size = 2
        self.piece_size = 50
        self.action_space = Discrete(11)  # 11 is the number of possible moves
        self.action_move = Action()       # Actions that cube can perform
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

    def get_position_array_row_size(self):
        return self.position_array_row_size

    def get_piece_size(self):
        return self.piece_size

    def get_cube_colors(self):
        return self.cube_colors

    def get_num_faces(self):
        return self.num_faces

    def get_num_pieces_per_face(self):
        return self.num_pieces_per_face

    def get_num_pieces_per_row(self):
        return self.num_pieces_per_row

    def get_num_pieces_per_col(self):
        return self.num_pieces_per_col

    def init_colors(self):
        """ Initialize colors of each piece of the cube """
        for side in range(self.num_faces):
            for row in range(self.num_pieces_per_row):
                for col in range(self.num_pieces_per_col):
                    self.cube_colors[side][row][col] = side

    def step(self, action):
        """ Perform an Action on the environment
            :param action: int
                Discrete number between 0 and 11 (Avalaible moves to rotate cube)
        """
        assert self.episode_started_at is not None, "Cannot call env.step() before calling reset()"
        assert self.action_space.contains(
            action) is not None, "%r is invalid action" % action
        self.action_move.rotate_cube(self.cube_colors, Moves(action))
        if self.is_solved():
            reward = 1.0
            done = True
        else:
            reward = self.action_reward.calculate_reward_pieces_position(
                self.cube_colors) / 100
            # reward = self.action_reward.calculate_reward(self.cube_colors) / 100
            done = False
        return self.cube_colors, reward, done

    def is_solved(self):
        """ Check if the cube is solved """
        for face in range(self.num_faces):
            for row in range(self.num_pieces_per_row):
                for col in range(self.num_pieces_per_col):
                    if self.cube_colors[face][row][col] != face:
                        return False
        return True

    def reset(self):
        """ Reset environment
            return: numpy array
                initial observation
        """
        self.init_colors()
        self.action_move.super_flip_configuration(self.cube_colors)
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

    def play(self, fps=30, callback=None):
        """ Play the game manually """
        game.play(self, fps=fps, callback=callback)


def make():
    """ Get an instance of the Cube environment """
    return Cube()
