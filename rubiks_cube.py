import random
import numpy as np
import rendering
import play as game
from space import Moves
from space import Discrete
import time

class Cube:
    """ Rubik's Cube Environment """
    def __init__(self):
        self.num_faces = 6
        self.num_pieces_per_face = 9    # size of cube => 9 for 3x3 cube, 16 for 4x4 cube ...
        self.num_pieces_per_row = int(np.sqrt(self.num_pieces_per_face))
        self.num_pieces_per_col = self.num_pieces_per_row
        self.cube_colors = np.full((self.num_faces, self.num_pieces_per_row, self.num_pieces_per_col), 0)
        self.position_array_row_size = 2
        self.piece_size = 50
        self.action_space = Discrete(11)
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

    def rotate_top(self):
        """ Rotate Top face of a cube clockwise (U move to the right) """
        cube = self.cube_colors

        swap1 = cube[1][0][0]
        swap2 = cube[1][0][1]
        swap3 = cube[1][0][2]

        cube[1][0][0] = cube[2][0][0]
        cube[2][0][0] = cube[3][0][0]
        cube[3][0][0] = cube[4][0][0]
        cube[4][0][0] = swap1

        cube[1][0][1] = cube[2][0][1]
        cube[2][0][1] = cube[3][0][1]
        cube[3][0][1] = cube[4][0][1]
        cube[4][0][1] = swap2

        cube[1][0][2] = cube[2][0][2]
        cube[2][0][2] = cube[3][0][2]
        cube[3][0][2] = cube[4][0][2]
        cube[4][0][2] = swap3

        swap_corner = cube[0][0][0]
        cube[0][0][0] = cube[0][2][0]
        cube[0][2][0] = cube[0][2][2]
        cube[0][2][2] = cube[0][0][2]
        cube[0][0][2] = swap_corner

        swap_middle = cube[0][0][1]
        cube[0][0][1] = cube[0][1][0]
        cube[0][1][0] = cube[0][2][1]
        cube[0][2][1] = cube[0][1][2]
        cube[0][1][2] = swap_middle

    def rotate_bottom(self):
        """ Rotate Bottom face of a cube clockwise (D move to the right) """
        cube = self.cube_colors

        swap1 = cube[1][2][0]
        swap2 = cube[1][2][1]
        swap3 = cube[1][2][2]

        cube[1][2][0] = cube[4][2][0]
        cube[4][2][0] = cube[3][2][0]
        cube[3][2][0] = cube[2][2][0]
        cube[2][2][0] = swap1


        cube[1][2][1] = cube[4][2][1]
        cube[4][2][1] = cube[3][2][1]
        cube[3][2][1] = cube[2][2][1]
        cube[2][2][1] = swap2

        cube[1][2][2] = cube[4][2][2]
        cube[4][2][2] = cube[3][2][2]
        cube[3][2][2] = cube[2][2][2]
        cube[2][2][2] = swap3

        swap_corner = cube[5][0][0]
        cube[5][0][0] = cube[5][2][0]
        cube[5][2][0] = cube[5][2][2]
        cube[5][2][2] = cube[5][0][2]
        cube[5][0][2] = swap_corner

        swap_middle = cube[5][0][1]
        cube[5][0][1] = cube[5][1][0]
        cube[5][1][0] = cube[5][2][1]
        cube[5][2][1] = cube[5][1][2]
        cube[5][1][2] = swap_middle

    def rotate_right(self):
        """ Rotate Right face of a cube clockwise (R move to the right) """
        cube = self.cube_colors

        swap1 = cube[0][0][2]
        swap2 = cube[0][1][2]
        swap3 = cube[0][2][2]

        cube[0][0][2] = cube[2][0][2]
        cube[2][0][2] = cube[5][0][2]
        cube[5][0][2] = cube[4][2][0]
        cube[4][2][0] = swap1

        cube[0][1][2] = cube[2][1][2]
        cube[2][1][2] = cube[5][1][2]
        cube[5][1][2] = cube[4][1][0]
        cube[4][1][0] = swap2

        cube[0][2][2] = cube[2][2][2]
        cube[2][2][2] = cube[5][2][2]
        cube[5][2][2] = cube[4][0][0]
        cube[4][0][0] = swap3

        swap_corner = cube[3][0][0]
        cube[3][0][0] = cube[3][2][0]
        cube[3][2][0] = cube[3][2][2]
        cube[3][2][2] = cube[3][0][2]
        cube[3][0][2] = swap_corner

        swap_middle = cube[3][0][1]
        cube[3][0][1] = cube[3][1][0]
        cube[3][1][0] = cube[3][2][1]
        cube[3][2][1] = cube[3][1][2]
        cube[3][1][2] = swap_middle

    def rotate_left(self):
        """ Rotate Left face of a cube clockwise (L move to the right) """
        cube = self.cube_colors

        swap1 = cube[0][0][0]
        swap2 = cube[0][1][0]
        swap3 = cube[0][2][0]

        cube[0][0][0] = cube[4][2][2]
        cube[4][2][2] = cube[5][0][0]
        cube[5][0][0] = cube[2][0][0]
        cube[2][0][0] = swap1

        cube[0][1][0] = cube[4][1][2]
        cube[4][1][2] = cube[5][1][0]
        cube[5][1][0] = cube[2][1][0]
        cube[2][1][0] = swap2

        cube[0][2][0] = cube[4][0][2]
        cube[4][0][2] = cube[5][2][0]
        cube[5][2][0] = cube[2][2][0]
        cube[2][2][0] = swap3

        swap_corner = cube[1][0][0]
        cube[1][0][0] = cube[1][2][0]
        cube[1][2][0] = cube[1][2][2]
        cube[1][2][2] = cube[1][0][2]
        cube[1][0][2] = swap_corner

        swap_middle = cube[1][0][1]
        cube[1][0][1] = cube[1][1][0]
        cube[1][1][0] = cube[1][2][1]
        cube[1][2][1] = cube[1][1][2]
        cube[1][1][2] = swap_middle

    def rotate_front(self):
        """ Rotate Front face of a cube clockwise (F move to the right) """
        cube = self.cube_colors

        swap1 = cube[0][2][0]
        swap2 = cube[0][2][1]
        swap3 = cube[0][2][2]

        cube[0][2][0] = cube[1][2][2]
        cube[1][2][2] = cube[5][0][2]
        cube[5][0][2] = cube[3][0][0]
        cube[3][0][0] = swap1

        cube[0][2][1] = cube[1][1][2]
        cube[1][1][2] = cube[5][0][1]
        cube[5][0][1] = cube[3][1][0]
        cube[3][1][0] = swap2

        cube[0][2][2] = cube[1][0][2]
        cube[1][0][2] = cube[5][0][0]
        cube[5][0][0] = cube[3][2][0]
        cube[3][2][0] = swap3

        swap_corner = cube[2][0][0]
        cube[2][0][0] = cube[2][2][0]
        cube[2][2][0] = cube[2][2][2]
        cube[2][2][2] = cube[2][0][2]
        cube[2][0][2] = swap_corner

        swap_middle = cube[2][0][1]
        cube[2][0][1] = cube[2][1][0]
        cube[2][1][0] = cube[2][2][1]
        cube[2][2][1] = cube[2][1][2]
        cube[2][1][2] = swap_middle

    def rotate_back(self):
        """ Rotate Back face of a cube clockwise (B move to the right) """
        cube = self.cube_colors

        swap1 = cube[0][0][0]
        swap2 = cube[0][0][1]
        swap3 = cube[0][0][2]

        cube[0][0][0] = cube[3][0][2]
        cube[3][0][2] = cube[5][2][2]
        cube[5][2][2] = cube[1][2][0]
        cube[1][2][0] = swap1

        cube[0][0][1] = cube[3][1][2]
        cube[3][1][2] = cube[5][2][1]
        cube[5][2][1] = cube[1][1][0]
        cube[1][1][0] = swap2

        cube[0][0][2] = cube[3][2][2]
        cube[3][2][2] = cube[5][2][0]
        cube[5][2][0] = cube[1][0][0]
        cube[1][0][0] = swap3


        swap_corner = cube[4][0][0]
        cube[4][0][0] = cube[4][2][0]
        cube[4][2][0] = cube[4][2][2]
        cube[4][2][2] = cube[4][0][2]
        cube[4][0][2] = swap_corner

        swap_middle = cube[4][0][1]
        cube[4][0][1] = cube[4][1][0]
        cube[4][1][0] = cube[4][2][1]
        cube[4][2][1] = cube[4][1][2]
        cube[4][1][2] = swap_middle

    def rotate_cube(self, move):
        """ Rotate the cube by the move
            :param move: Enum space.Moves()
        """
        if move == Moves.U:
            self.rotate_top()
        elif move == Moves.Ui:
            self.rotate_cube_reverse(Moves.U)
        elif move == Moves.D:
            self.rotate_bottom()
        elif move == Moves.Di:
            self.rotate_cube_reverse(Moves.D)
        elif move == Moves.L:
            self.rotate_left()
        elif move == Moves.Li:
            self.rotate_cube_reverse(Moves.L)
        elif move == Moves.R:
            self.rotate_right()
        elif move == Moves.Ri:
            self.rotate_cube_reverse(Moves.R)
        elif move == Moves.F:
            self.rotate_front()
        elif move == Moves.Fi:
            self.rotate_cube_reverse(Moves.F)
        elif move == Moves.B:
            self.rotate_back()
        elif move == Moves.Bi:
            self.rotate_cube_reverse(Moves.B)

    def step(self, action):
        """ Perform an Action on the environment
            :param action: int
                Discrete number between 0 and 11 (Avalaible moves to rotate cube)
        """
        assert self.episode_started_at is not None, "Cannot call env.step() before calling reset()"
        assert self.action_space.contains(action) is not None, "%r is invalid action" % action
        self.rotate_cube(Moves(action))
        if self.is_solved():
            reward = 1.0
            done = True
        else:
            reward = self.calculate_reward_pieces_position() / 100
            # reward = self.calculate_reward() / 100
            done = False
        return self.cube_colors, reward, done

    def rotate_cube_reverse(self, move):
        """ Rotate the cube in reverse move
            :param move: Enum space.Moves()

            This function will perform given move 3 time which is
            equivalent to rotate cube in oposite move,
            for example, U move becomes U' -> 3x U move
        """
        for _ in range(3):
            self.rotate_cube(move)

    def random_shuffle(self, number):
        """ Randomly shuffle the cube
            :param number: int
                Number of random moves performed by random generator
            :return sequence: String
                Sequence of performed moves
        """
        sequence = ""
        for _ in range(number):
            choice = random.choice(["U", "D", "L", "R", "F", "B", "Ui", "Di", "Li", "Ri", "Fi", "Bi"])
            self.rotate_cube(Moves[choice])
            sequence += choice
        return sequence

    def sort_cube(self, list_choices):
        """ Sort the cube by the moves stored in list
            :param list_choices: Array List of Strings
                Each string is a move to rotate cube
            The List is Reversed before the iteration and
            each move is done 3 times which rotates cube in
            oposite direction of the given move
        """
        for choice in reversed(list_choices):
            self.rotate_cube_reverse(Moves[choice])

    def is_solved(self):
        """ Check if the cube is solved """
        for face in range(self.num_faces):
            for row in range(self.num_pieces_per_row):
                for col in range(self.num_pieces_per_col):
                    if self.cube_colors[face][row][col] != face:
                        return False
        return True

    def super_flip_configuration(self):
        """ This is a rubics cube configuration where the cube is most scrumbled """
        list_of_moves = ["U", "R", "R", "F", "B", "R", "B", "B", "R", "U", "U", "L", "B", "B", "R", "Ui", "Di", "R", "R", "F", "Ri", "L", "B", "B", "U", "U", "F", "F"]
        # list_of_moves = [0 ,6, 6, 8, 10, 6, 10, 10, 6, 0, 0, 4, 10, 10, 6, 1, 3, 6, 6, 8, 7, 4, 10, 10, 0, 0, 8, 8]
        for move in list_of_moves:
            self.rotate_cube(Moves[move])
            # self.rotate_cube(Moves(move))

    def reset(self):
        """ Reset environment
            return: numpy array
                initial observation
        """
        self.init_colors()
        # self.super_flip_configuration()
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

    def calculate_reward(self):
        """ Calculate reward for each move
            The reword is calculated by iterating over
            the cube colors array and if the color is
            the face color, then add one to the counter
            of correct pieces. After iteration is finished,
            correct pieces number is divided by the number of
            the total pieces of the cube and multiply by 100
            which gives the reward represented as percentage.

            return: float
                Percentage of the cube solved

        """
        correct_pieces = 0
        for face in range(self.num_faces):
            for row in range(self.num_pieces_per_row):
                for col in range(self.num_pieces_per_col):
                    if self.cube_colors[face][row][col] == face:
                        correct_pieces += 1
        return correct_pieces / 54 * 100

    def calculate_reward_pieces_position(self):
        """ Calculate reward base on pieces position
        """
        correct_pieces = 0
        correct_pieces += self.get_num_correct_corners()
        correct_pieces += self.get_num_correct_edges()
        return correct_pieces / 20 * 100

    def get_num_correct_corners(self):
        """ Get number of corner pieces that are on correct position """
        number_correct_corners = 0
        # W0 G0 O6    0,0,0   1,0,0   4,0,2
        if self.cube_colors[0][0][0] == 0 and self.cube_colors[1][0][0] == 1 and self.cube_colors[4][0][2] == 4:
            number_correct_corners += 1
        # W2 G6 R0    0,2,0   1,0,2   2,0,0
        if self.cube_colors[0][2][0] == 0 and self.cube_colors[1][0][2] == 1 and self.cube_colors[2][0][0] == 2:
            number_correct_corners += 1
        # W6 6B O0    0,0,2   3,0,2   4,0,0
        if self.cube_colors[0][0][2] == 0 and self.cube_colors[3][0][2] == 3 and self.cube_colors[4][0][0] == 4:
            number_correct_corners += 1
        # W8 R6 B0    0,2,2   2,0,2   3,0,0
        if self.cube_colors[0][2][2] == 0 and self.cube_colors[2][0][2] == 2 and self.cube_colors[3][0][0] == 3:
            number_correct_corners += 1
        # Y0 G8 R2    5,0,0   1,2,2   2,2,0
        if self.cube_colors[5][0][0] == 5 and self.cube_colors[1][2][2] == 1 and self.cube_colors[2][2][0] == 2:
            number_correct_corners += 1
        # Y2 G2 O8    5,2,0   1,2,0   4,2,2
        if self.cube_colors[5][2][0] == 5 and self.cube_colors[1][2][0] == 1 and self.cube_colors[4][2][2] == 4:
            number_correct_corners += 1
           # Y6 R8 B2    5,0,2   2,2,2   3,2,0
        if self.cube_colors[5][0][2] == 5 and self.cube_colors[2][2][2] == 2 and self.cube_colors[3][2][0] == 3:
            number_correct_corners += 1
        # Y8 B8 O2    5,2,2   3,2,2   4,2,0
        if self.cube_colors[5][2][2] == 5 and self.cube_colors[3][2][2] == 3 and self.cube_colors[4][2][0] == 4:
            number_correct_corners += 1
        return number_correct_corners

    def get_num_correct_edges(self):
        """ Get number of edge pieces that are on correct position """
        number_correct_edges = 0
        # 0,0,1   4,0,1
        if self.cube_colors[0][0][1] == 0 and self.cube_colors[4][0][1] == 4:
            number_correct_edges += 1
        # 0,1,0   1,0,1
        if self.cube_colors[0][1][0] == 0 and self.cube_colors[1][0][1] == 1:
            number_correct_edges += 1
        # 0,1,2   3,0,1
        if self.cube_colors[0][1][2] == 0 and self.cube_colors[3][0][1] == 3:
            number_correct_edges += 1
        # 0,2,1   2,0,1
        if self.cube_colors[0][2][1] == 0 and self.cube_colors[2][0][1] == 2:
            number_correct_edges += 1
        # 5,0,1   2,2,1
        if self.cube_colors[5][0][1] == 5 and self.cube_colors[2][2][1] == 2:
            number_correct_edges += 1
        # 5,1,0   1,2,1
        if self.cube_colors[5][1][0] == 5 and self.cube_colors[1][2][1] == 1:
            number_correct_edges += 1
        # 5,1,2   3,2,1
        if self.cube_colors[5][1][2] == 5 and self.cube_colors[3][2][1] == 3:
            number_correct_edges += 1
        # 5,2,1   4,2,1
        if self.cube_colors[5][2][1] == 5 and self.cube_colors[4][2][1] == 4:
            number_correct_edges += 1
        # 1,1,0   4,1,2
        if self.cube_colors[1][1][0] == 1 and self.cube_colors[4][1][2] == 4:
            number_correct_edges += 1
        # 1,1,2   2,1,0
        if self.cube_colors[1][1][2] == 1 and self.cube_colors[2][1][0] == 2:
            number_correct_edges += 1
        # 3,1,0   2,1,2
        if self.cube_colors[3][1][0] == 3 and self.cube_colors[2][1][2] == 2:
            number_correct_edges += 1
        # 3,1,2   4,1,0
        if self.cube_colors[3][1][2] == 3 and self.cube_colors[4][1][0] == 4:
            number_correct_edges += 1
        return number_correct_edges

    def close(self):
        """ Close the rendering window """
        self.view.close()

    def play(self, fps=30, callback=None):
        """ Play the game manually """
        game.play(self, fps=fps, callback=callback)

def make():
    """ Get an instance of the Cube environment """
    return Cube()