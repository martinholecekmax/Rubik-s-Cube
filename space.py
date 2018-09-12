from enum import Enum
import random
import numpy as np

class Moves(Enum):
    U = 0
    Ui = 1
    D = 2
    Di = 3
    L = 4
    Li = 5
    R = 6
    Ri = 7
    F = 8
    Fi = 9
    B = 10
    Bi = 11

class Action:
    def __init__(self, env):
        self.env = env

    def init_colors(self, cube_colors):
        """ Initialize colors of each piece of the cube """
        for side in range(self.env.num_faces):
            for row in range(self.env.num_pieces_per_row):
                for col in range(self.env.num_pieces_per_col):
                    cube_colors[side][row][col] = side

    def is_solved(self, cube_colors):
        """ Check if the cube is solved """
        for face in range(self.env.num_faces):
            for row in range(self.env.num_pieces_per_row):
                for col in range(self.env.num_pieces_per_col):
                    if cube_colors[face][row][col] != face:
                        return False
        return True

    def rotate_top(self, cube):
        """ Rotate Top face of a cube clockwise (U move to the right) """

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

        swap_edges = cube[0][0][1]
        cube[0][0][1] = cube[0][1][0]
        cube[0][1][0] = cube[0][2][1]
        cube[0][2][1] = cube[0][1][2]
        cube[0][1][2] = swap_edges

    def rotate_bottom(self, cube):
        """ Rotate Bottom face of a cube clockwise (D move to the right) """

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

        swap_edges = cube[5][0][1]
        cube[5][0][1] = cube[5][1][0]
        cube[5][1][0] = cube[5][2][1]
        cube[5][2][1] = cube[5][1][2]
        cube[5][1][2] = swap_edges

    def rotate_right(self, cube):
        """ Rotate Right face of a cube clockwise (R move to the right) """

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

        swap_edges = cube[3][0][1]
        cube[3][0][1] = cube[3][1][0]
        cube[3][1][0] = cube[3][2][1]
        cube[3][2][1] = cube[3][1][2]
        cube[3][1][2] = swap_edges

    def rotate_left(self, cube):
        """ Rotate Left face of a cube clockwise (L move to the right) """

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

        swap_edges = cube[1][0][1]
        cube[1][0][1] = cube[1][1][0]
        cube[1][1][0] = cube[1][2][1]
        cube[1][2][1] = cube[1][1][2]
        cube[1][1][2] = swap_edges

    def rotate_front(self, cube):
        """ Rotate Front face of a cube clockwise (F move to the right) """

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

        swap_edges = cube[2][0][1]
        cube[2][0][1] = cube[2][1][0]
        cube[2][1][0] = cube[2][2][1]
        cube[2][2][1] = cube[2][1][2]
        cube[2][1][2] = swap_edges

    def rotate_back(self, cube):
        """ Rotate Back face of a cube clockwise (B move to the right) """

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

        swap_edges = cube[4][0][1]
        cube[4][0][1] = cube[4][1][0]
        cube[4][1][0] = cube[4][2][1]
        cube[4][2][1] = cube[4][1][2]
        cube[4][1][2] = swap_edges

    def rotate_cube(self, cube, move):
        """ Rotate the cube by the move
            :param cube: Numpy array
                Colors of the cube stored in numpy array
            :param move: Enum Moves()
        """
        if move == Moves.U:
            self.rotate_top(cube)
        elif move == Moves.Ui:
            self.rotate_cube_reverse(cube, Moves.U)
        elif move == Moves.D:
            self.rotate_bottom(cube)
        elif move == Moves.Di:
            self.rotate_cube_reverse(cube, Moves.D)
        elif move == Moves.L:
            self.rotate_left(cube)
        elif move == Moves.Li:
            self.rotate_cube_reverse(cube, Moves.L)
        elif move == Moves.R:
            self.rotate_right(cube)
        elif move == Moves.Ri:
            self.rotate_cube_reverse(cube, Moves.R)
        elif move == Moves.F:
            self.rotate_front(cube)
        elif move == Moves.Fi:
            self.rotate_cube_reverse(cube, Moves.F)
        elif move == Moves.B:
            self.rotate_back(cube)
        elif move == Moves.Bi:
            self.rotate_cube_reverse(cube, Moves.B)

    def rotate_cube_reverse(self,cube, move):
        """ Rotate the cube in reverse move
            :param move: Enum space.Moves()

            This function will perform given move 3 time which is
            equivalent to rotate cube in oposite move,
            for example, U move becomes U' -> 3x U move
        """
        for _ in range(3):
            self.rotate_cube(cube, move)

    def random_shuffle(self, cube, number):
        """ Randomly shuffle the cube
            :param number: int
                Number of random moves performed by random generator
            :return sequence: String
                Sequence of performed moves
        """
        sequence = ""
        for _ in range(number):
            choice = random.choice(["U", "D", "L", "R", "F", "B", "Ui", "Di", "Li", "Ri", "Fi", "Bi"])
            self.rotate_cube(cube, Moves[choice])
            sequence += choice
        return sequence

    def scramble_cube_from_list(self, cube, list_moves):
        """ Scramble the cube by the moves from the array list
            :param list_moves: Array List of Strings or Integers
                Each element is a move that will rotate the cube
                The elements of the list can be either numeric
                representation of the move (values between 0 and 11),
                or string values (U, Ui, D, Di, L, Li, R, Ri, F, Fi, B, Bi)
                which are case insensitive and can be either uppercase, lower case or mixed.
        """
        is_number = all(isinstance(i, int) for i in list_moves)
        if is_number:
            is_number = all(i >= 0 and i <= 11 for i in list_moves)
            if not is_number:
                assert False, "Out of bounds, only numbers between 0 and 11 are allowed!"
            else:
                for move in list_moves:
                    self.rotate_cube(cube, Moves(move))
        else:
            is_string = set([move.capitalize() for move in list_moves]).issubset([move.name for move in Moves])
            if is_string:
                for move in list_moves:
                    self.rotate_cube(cube, Moves[move.capitalize()])
            else:
                assert False, "Invalid moves, available moves: U, Ui, D, Di, L, Li, R, Ri, F, Fi, B, Bi"

    def super_flip_configuration(self, cube):
        """ This is the configuration where the cube is the most scrumbled """
        list_of_moves = ["U", "R", "R", "F", "B", "R", "B", "B", "R", "U", "U", "L", "B", "B", "R", "Ui", "Di", "R", "R", "F", "Ri", "L", "B", "B", "U", "U", "F", "F"]
        # list_of_moves = [0 ,6, 6, 8, 10, 6, 10, 10, 6, 0, 0, 4, 10, 10, 6, 1, 3, 6, 6, 8, 7, 4, 10, 10, 0, 0, 8, 8]
        for move in list_of_moves:
            self.rotate_cube(cube, Moves[move])
            # self.rotate_cube(cube, Moves(move))

class Discrete():
    def __init__(self, num_actions):
        self.num_actions = num_actions

    def contains(self, x):
        if isinstance(x, int):
            return x >= 0 and x < self.num_actions
        else:
            return False

    def sample(self):
        return random.randint(0, self.num_actions)

    def __repr__(self):
        return "Discrete(%d)" % self.num_actions
