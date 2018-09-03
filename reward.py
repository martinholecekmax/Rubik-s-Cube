
class Reward:
    def __init__(self, env):
        self.num_faces = env.get_num_faces()
        self.num_pieces_per_row = env.get_num_pieces_per_row()
        self.num_pieces_per_col = env.get_num_pieces_per_col()

    def calculate_reward_pieces_color(self, cube):
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

    def calculate_reward_pieces_position(self, cube):
        """ Calculate reward base on pieces position
        """
        correct_pieces = 0
        correct_pieces += self.get_num_correct_corners(cube)
        correct_pieces += self.get_num_correct_edges(cube)
        return correct_pieces / 20 * 100

    def get_num_correct_corners(self, cube_colors):
        """ Get number of corner pieces that are on correct position """
        number_correct_corners = 0
        # W0 G0 O6    0,0,0   1,0,0   4,0,2
        if cube_colors[0][0][0] == 0 and cube_colors[1][0][0] == 1 and cube_colors[4][0][2] == 4:
            number_correct_corners += 1
        # W2 G6 R0    0,2,0   1,0,2   2,0,0
        if cube_colors[0][2][0] == 0 and cube_colors[1][0][2] == 1 and cube_colors[2][0][0] == 2:
            number_correct_corners += 1
        # W6 6B O0    0,0,2   3,0,2   4,0,0
        if cube_colors[0][0][2] == 0 and cube_colors[3][0][2] == 3 and cube_colors[4][0][0] == 4:
            number_correct_corners += 1
        # W8 R6 B0    0,2,2   2,0,2   3,0,0
        if cube_colors[0][2][2] == 0 and cube_colors[2][0][2] == 2 and cube_colors[3][0][0] == 3:
            number_correct_corners += 1
        # Y0 G8 R2    5,0,0   1,2,2   2,2,0
        if cube_colors[5][0][0] == 5 and cube_colors[1][2][2] == 1 and cube_colors[2][2][0] == 2:
            number_correct_corners += 1
        # Y2 G2 O8    5,2,0   1,2,0   4,2,2
        if cube_colors[5][2][0] == 5 and cube_colors[1][2][0] == 1 and cube_colors[4][2][2] == 4:
            number_correct_corners += 1
        # Y6 R8 B2    5,0,2   2,2,2   3,2,0
        if cube_colors[5][0][2] == 5 and cube_colors[2][2][2] == 2 and cube_colors[3][2][0] == 3:
            number_correct_corners += 1
        # Y8 B8 O2    5,2,2   3,2,2   4,2,0
        if cube_colors[5][2][2] == 5 and cube_colors[3][2][2] == 3 and cube_colors[4][2][0] == 4:
            number_correct_corners += 1
        return number_correct_corners

    def get_num_correct_edges(self, cube_colors):
        """ Get number of edge pieces that are on correct position """
        number_correct_edges = 0
        # 0,0,1   4,0,1
        if cube_colors[0][0][1] == 0 and cube_colors[4][0][1] == 4:
            number_correct_edges += 1
        # 0,1,0   1,0,1
        if cube_colors[0][1][0] == 0 and cube_colors[1][0][1] == 1:
            number_correct_edges += 1
        # 0,1,2   3,0,1
        if cube_colors[0][1][2] == 0 and cube_colors[3][0][1] == 3:
            number_correct_edges += 1
        # 0,2,1   2,0,1
        if cube_colors[0][2][1] == 0 and cube_colors[2][0][1] == 2:
            number_correct_edges += 1
        # 5,0,1   2,2,1
        if cube_colors[5][0][1] == 5 and cube_colors[2][2][1] == 2:
            number_correct_edges += 1
        # 5,1,0   1,2,1
        if cube_colors[5][1][0] == 5 and cube_colors[1][2][1] == 1:
            number_correct_edges += 1
        # 5,1,2   3,2,1
        if cube_colors[5][1][2] == 5 and cube_colors[3][2][1] == 3:
            number_correct_edges += 1
        # 5,2,1   4,2,1
        if cube_colors[5][2][1] == 5 and cube_colors[4][2][1] == 4:
            number_correct_edges += 1
        # 1,1,0   4,1,2
        if cube_colors[1][1][0] == 1 and cube_colors[4][1][2] == 4:
            number_correct_edges += 1
        # 1,1,2   2,1,0
        if cube_colors[1][1][2] == 1 and cube_colors[2][1][0] == 2:
            number_correct_edges += 1
        # 3,1,0   2,1,2
        if cube_colors[3][1][0] == 3 and cube_colors[2][1][2] == 2:
            number_correct_edges += 1
        # 3,1,2   4,1,0
        if cube_colors[3][1][2] == 3 and cube_colors[4][1][0] == 4:
            number_correct_edges += 1
        return number_correct_edges
