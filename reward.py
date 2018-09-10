
class Reward:
    def __init__(self, env):
        self.num_faces = env.get_num_faces()
        self.num_pieces_per_row = env.get_num_pieces_per_row()
        self.num_pieces_per_col = env.get_num_pieces_per_col()
        self.last_reward = 0
        self.cube_colors = env.cube_colors

    def calculate_reward(self):
        """ This function allows to choose which way to calculate reward. """
        # return self.calculate_reward_pieces_color()
        return self.calculate_reward_pieces_position()

    def calculate_reward_pieces_color(self):
        """ Calculate reward for each move based on number of pieces color that are correct for each wall.
            return: float
                Normalized value between -1 and 1 of the correct pieces of the cube
        """
        correct_pieces = 0
        for face in range(self.num_faces):
            for row in range(self.num_pieces_per_row):
                for col in range(self.num_pieces_per_col):
                    if self.cube_colors[face][row][col] == face:
                        correct_pieces += 1
        # reward = self.normalization(correct_pieces, 54, 0, 0, 1)    # Normalization (reward is number between 0.0 and 1.0)
        reward = self.normalization(correct_pieces, 54, 0, -1, 1)  # Normalization (reward is number between -1.0 and 1.0)
        self.last_reward = reward
        return reward

    def calculate_reward_pieces_position(self):
        """ Calculate reward by checking if each piece is in correct position.
            return: float
                Normalized value between -1 and 1 of the correct pieces of the cube
        """
        correct_pieces = 0
        num_edges = 12
        num_corners = 8
        correct_pieces += self.get_num_correct_corners(self.cube_colors)
        correct_pieces += self.get_num_correct_edges(self.cube_colors)
        # reward = self.normalization(correct_pieces, num_corners + num_edges, 0, 0, 1)   # Normalization (reward is number between 0.0 and 1.0)
        reward = self.normalization(correct_pieces, num_corners + num_edges, 0, -1, 1)  # Normalization (reward is number between -1.0 and 1.0)
        self.last_reward = reward
        return reward

    def normalization(self, x, x_max, x_min, a, b):
        """ Normalization formula
            x - value to be normalized
            x_max - max value of x
            x_min - min value of x
            a, b - range of normalization (a - min, b - max)
        """
        norm = (b - a) * ( ( x - x_min ) / ( x_max - x_min) ) + a
        return norm

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
