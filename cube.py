import random
import numpy as np

class Cube:
    piece_size = 50
    num_faces = 6
    num_pieces_per_face = 9    # size of cube => 9 for 3x3 cube, 16 for 4x4 cube ...
    num_pieces_per_row = int(np.sqrt(num_pieces_per_face))
    num_pieces_per_col = num_pieces_per_row
    row_size = 2    # 0 - x position, 1 - y position
    cube_position = np.full((num_faces, num_pieces_per_row, num_pieces_per_col, row_size), 0)
    cube_colors = np.full((num_faces, num_pieces_per_row, num_pieces_per_col), 0)

    def get_cube_colors(self):
        return self.cube_colors

    def get_cube(self):
        return self.cube_position

    def get_piece_size(self):
        return self.piece_size

    def get_num_faces(self):
        return self.num_faces

    def get_num_pieces_per_face(self):
        return self.num_pieces_per_face

    def get_num_pieces_per_row(self):
        return self.num_pieces_per_row

    def get_num_pieces_per_col(self):
        return self.num_pieces_per_col

    def get_row_size(self):
        return self.row_size

    def init_colors(self):
        """ Initialize colors of each piece of the cube """
        for side in range(self.num_faces):
            for row in range(self.num_pieces_per_row):
                for col in range(self.num_pieces_per_col):
                    self.cube_colors[side][row][col] = side

    def init_cube(self):
        """ Initialize positions of each piece of the cube """
        num_faces = self.num_faces
        num_pieces_per_face = self.num_pieces_per_face
        cube_array_row_size = self.row_size
        num_pieces_per_row = self.num_pieces_per_row
        num_pieces_per_col = self.num_pieces_per_col
        piece_size = self.piece_size
        cube = self.cube_position

        column_position = piece_size
        row_position = piece_size
        face_column_position = num_pieces_per_col * piece_size     # First face has one face offset
        face_row_position = 0

        for side in range(num_faces):
            for row in range(num_pieces_per_row):
                for col in range(num_pieces_per_col):
                    cube[side][row][col][0] = column_position + face_column_position
                    cube[side][row][col][1] = row_position + face_row_position
                    column_position += piece_size
                row_position += piece_size
                column_position = piece_size
            row_position = piece_size
            column_position = piece_size
            face_column_position += num_pieces_per_col * piece_size
            if side == 0:
                face_row_position += num_pieces_per_row * piece_size    # face offset in horizontal direction
                face_column_position = 0
            if side == 4:
                face_column_position = num_pieces_per_col * piece_size  # face offset in horizontal direction
                face_row_position += num_pieces_per_row * piece_size    # face offset in vertical direction

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
        """ Rotate the cube by the move """
        if move == "U":
            self.rotate_top()
            return "U"
        elif move == "D":
            self.rotate_bottom()
            return "D"
        elif move == "L":
            self.rotate_left()
            return "L"
        elif move == "R":
            self.rotate_right()
            return "R"
        elif move == "F":
            self.rotate_front()
            return "F"
        elif move == "B":
            self.rotate_back()
            return "B"
        else:
            return "?"

    def rotate_cube_reverse(self, move):
        """ Rotate the cube in reverse move, for example, U move becomes U' -> 3x U move """
        for _ in range(3):
                self.rotate_cube(move)

    def random_shuffle(self, number):
        """ Randomly shuffle the cube """
        sequence = ""
        for _ in range(number):
            choice = random.choice(["U", "D", "L", "R", "F", "B"])
            sequence += self.rotate_cube(choice)
        return sequence

    def sort_cube(self, list_choices):
        """ Sort the cube by the moves stored in list """
        # Reverse list before the iteration
        for choice in reversed(list_choices):
            self.rotate_cube_reverse(choice)

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
        list_of_moves = ["U", "R", "R", "F", "B", "R", "B", "B", "R", "U", "U", "L", "B", "B", "R", "U", "U", "U", "D", "D", "D", "R", "R", "F", "R", "R", "R", "L", "B", "B", "U", "U", "F", "F"]
        for move in list_of_moves:
            self.rotate_cube(move)
