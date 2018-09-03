from enum import Enum
import random


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

    def sort_cube(self, cube, list_choices):
        """ Sort the cube by the moves stored in list
            :param list_choices: Array List of Strings
                Each string is a move to rotate cube
            The List is Reversed before the iteration and
            each move is done 3 times which rotates cube in
            oposite direction of the given move
        """
        for choice in reversed(list_choices):
            self.rotate_cube_reverse(cube, Moves[choice])

    def super_flip_configuration(self, cube):
        """ This is a rubics cube configuration where the cube is most scrumbled """
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
