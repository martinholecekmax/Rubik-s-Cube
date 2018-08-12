import random
import numpy as np

class Cube:
    piece_size = 50
    num_faces = 6
    num_pieces_per_face = 9    # size of cube => 9 for 3x3 cube, 16 for 4x4 cube ...
    num_pieces_per_row = np.sqrt(num_pieces_per_face)
    row_size = 3    # 0 - color, 1 - x position, 2 - y position
    cube_array = np.full((num_faces, num_pieces_per_face, row_size), 0)

    def get_cube(self):
        return self.cube_array

    def get_piece_size(self):
        return self.piece_size

    def get_num_faces(self):
        return self.num_faces

    def get_num_pieces_per_face(self):
        return self.num_pieces_per_face

    def get_row_size(self):
        return self.row_size

    def init_cube(self):
        """ Initialize the cube
        """
        num_faces = self.num_faces
        num_pieces_per_face = self.num_pieces_per_face
        row_size = self.row_size
        num_pieces_per_row = self.num_pieces_per_row
        piece_size = self.piece_size
        cube = self.cube_array

        column_position = piece_size
        row_position = piece_size
        face_column_position = num_pieces_per_row * piece_size     # First face has one face offset
        face_row_position = 0
        for side in range(num_faces):
            for row in range(num_pieces_per_face):
                for col in range(row_size):
                    if col == 0:
                        cube[side][row][col] = side
                        if column_position > num_pieces_per_row * piece_size:
                            column_position = piece_size
                            row_position += piece_size
                        if row_position > num_pieces_per_row * piece_size:
                            row_position = piece_size
                    elif col == 1:
                        cube[side][row][col] = row_position + face_column_position
                    else:
                        cube[side][row][col] = column_position + face_row_position

                    # last piece in row increment row
                    if row_size - 1 == col:
                        column_position += piece_size
            face_column_position += num_pieces_per_row * piece_size
            if side == 0:
                face_row_position += num_pieces_per_row * piece_size
                face_column_position = 0
                column_position = piece_size
                row_position = piece_size
            if side == 4:
                # Last face has one face offset in horizontal direction
                face_column_position = num_pieces_per_row * piece_size
                # Last face has two face offset in vertical direction
                face_row_position = 2 * num_pieces_per_row * piece_size
                column_position = piece_size
                row_position = piece_size

    def rotate_top(self):
        """ Rotate Top face of a cube clockwise (U move to the right)
        """
        cube = self.cube_array

        swap1 = cube[1][0][0]
        swap2 = cube[1][3][0]
        swap3 = cube[1][6][0]

        cube[1][0][0] = cube[2][0][0]
        cube[2][0][0] = cube[3][0][0]
        cube[3][0][0] = cube[4][0][0]
        cube[4][0][0] = swap1

        cube[1][3][0] = cube[2][3][0]
        cube[2][3][0] = cube[3][3][0]
        cube[3][3][0] = cube[4][3][0]
        cube[4][3][0] = swap2

        cube[1][6][0] = cube[2][6][0]
        cube[2][6][0] = cube[3][6][0]
        cube[3][6][0] = cube[4][6][0]
        cube[4][6][0] = swap3

        swap_corner = cube[0][0][0]
        cube[0][0][0] = cube[0][2][0]
        cube[0][2][0] = cube[0][8][0]
        cube[0][8][0] = cube[0][6][0]
        cube[0][6][0] = swap_corner

        swap_middle = cube[0][1][0]
        cube[0][1][0] = cube[0][5][0]
        cube[0][5][0] = cube[0][7][0]
        cube[0][7][0] = cube[0][3][0]
        cube[0][3][0] = swap_middle

    def rotate_bottom(self):
        """ Rotate Bottom face of a cube clockwise (D move to the right)
        """
        cube = self.cube_array

        swap1 = cube[1][2][0]
        swap2 = cube[1][5][0]
        swap3 = cube[1][8][0]

        cube[1][2][0] = cube[4][2][0]
        cube[4][2][0] = cube[3][2][0]
        cube[3][2][0] = cube[2][2][0]
        cube[2][2][0] = swap1

        cube[1][5][0] = cube[4][5][0]
        cube[4][5][0] = cube[3][5][0]
        cube[3][5][0] = cube[2][5][0]
        cube[2][5][0] = swap2

        cube[1][8][0] = cube[4][8][0]
        cube[4][8][0] = cube[3][8][0]
        cube[3][8][0] = cube[2][8][0]
        cube[2][8][0] = swap3

        swap_corner = cube[5][0][0]
        cube[5][0][0] = cube[5][2][0]
        cube[5][2][0] = cube[5][8][0]
        cube[5][8][0] = cube[5][6][0]
        cube[5][6][0] = swap_corner

        swap_middle = cube[5][1][0]
        cube[5][1][0] = cube[5][5][0]
        cube[5][5][0] = cube[5][7][0]
        cube[5][7][0] = cube[5][3][0]
        cube[5][3][0] = swap_middle

    def rotate_right(self):
        """ Rotate Right face of a cube clockwise (R move to the right)
        """
        cube = self.cube_array

        swap1 = cube[0][6][0]
        swap2 = cube[0][7][0]
        swap3 = cube[0][8][0]

        cube[0][6][0] = cube[2][6][0]
        cube[2][6][0] = cube[5][6][0]
        cube[5][6][0] = cube[4][2][0]
        cube[4][2][0] = swap1

        cube[0][7][0] = cube[2][7][0]
        cube[2][7][0] = cube[5][7][0]
        cube[5][7][0] = cube[4][1][0]
        cube[4][1][0] = swap2

        cube[0][8][0] = cube[2][8][0]
        cube[2][8][0] = cube[5][8][0]
        cube[5][8][0] = cube[4][0][0]
        cube[4][0][0] = swap3

        swap_corner = cube[3][0][0]
        cube[3][0][0] = cube[3][2][0]
        cube[3][2][0] = cube[3][8][0]
        cube[3][8][0] = cube[3][6][0]
        cube[3][6][0] = swap_corner

        swap_middle = cube[3][1][0]
        cube[3][1][0] = cube[3][5][0]
        cube[3][5][0] = cube[3][7][0]
        cube[3][7][0] = cube[3][3][0]
        cube[3][3][0] = swap_middle

    def rotate_left(self):
        """ Rotate Left face of a cube clockwise (L move to the right)
        """
        cube = self.cube_array

        swap1 = cube[4][6][0]
        swap2 = cube[4][7][0]
        swap3 = cube[4][8][0]

        cube[4][6][0] = cube[5][2][0]
        cube[5][2][0] = cube[2][2][0]
        cube[2][2][0] = cube[0][2][0]
        cube[0][2][0] = swap1

        cube[4][7][0] = cube[5][1][0]
        cube[5][1][0] = cube[2][1][0]
        cube[2][1][0] = cube[0][1][0]
        cube[0][1][0] = swap2

        cube[4][8][0] = cube[5][0][0]
        cube[5][0][0] = cube[2][0][0]
        cube[2][0][0] = cube[0][0][0]
        cube[0][0][0] = swap3

        swap_corner = cube[1][0][0]
        cube[1][0][0] = cube[1][2][0]
        cube[1][2][0] = cube[1][8][0]
        cube[1][8][0] = cube[1][6][0]
        cube[1][6][0] = swap_corner

        swap_middle = cube[1][1][0]
        cube[1][1][0] = cube[1][5][0]
        cube[1][5][0] = cube[1][7][0]
        cube[1][7][0] = cube[1][3][0]
        cube[1][3][0] = swap_middle

    def rotate_front(self):
        """ Rotate Front face of a cube clockwise (F move to the right)
        """
        cube = self.cube_array

        swap1 = cube[0][2][0]
        swap2 = cube[0][5][0]
        swap3 = cube[0][8][0]

        cube[0][2][0] = cube[1][8][0]
        cube[1][8][0] = cube[5][6][0]
        cube[5][6][0] = cube[3][0][0]
        cube[3][0][0] = swap1

        cube[0][5][0] = cube[1][7][0]
        cube[1][7][0] = cube[5][3][0]
        cube[5][3][0] = cube[3][1][0]
        cube[3][1][0] = swap2

        cube[0][8][0] = cube[1][6][0]
        cube[1][6][0] = cube[5][0][0]
        cube[5][0][0] = cube[3][2][0]
        cube[3][2][0] = swap3

        swap_corner = cube[2][0][0]
        cube[2][0][0] = cube[2][2][0]
        cube[2][2][0] = cube[2][8][0]
        cube[2][8][0] = cube[2][6][0]
        cube[2][6][0] = swap_corner

        swap_middle = cube[2][1][0]
        cube[2][1][0] = cube[2][5][0]
        cube[2][5][0] = cube[2][7][0]
        cube[2][7][0] = cube[2][3][0]
        cube[2][3][0] = swap_middle

    def rotate_back(self):
        """ Rotate Back face of a cube clockwise (B move to the right)
        """
        cube = self.cube_array

        swap1 = cube[0][0][0]
        swap2 = cube[0][3][0]
        swap3 = cube[0][6][0]

        cube[0][0][0] = cube[3][6][0]
        cube[3][6][0] = cube[5][8][0]
        cube[5][8][0] = cube[1][2][0]
        cube[1][2][0] = swap1

        cube[0][3][0] = cube[3][7][0]
        cube[3][7][0] = cube[5][5][0]
        cube[5][5][0] = cube[1][1][0]
        cube[1][1][0] = swap2

        cube[0][6][0] = cube[3][8][0]
        cube[3][8][0] = cube[5][2][0]
        cube[5][2][0] = cube[1][0][0]
        cube[1][0][0] = swap3

        swap_corner = cube[4][0][0]
        cube[4][0][0] = cube[4][2][0]
        cube[4][2][0] = cube[4][8][0]
        cube[4][8][0] = cube[4][6][0]
        cube[4][6][0] = swap_corner

        swap_middle = cube[4][1][0]
        cube[4][1][0] = cube[4][5][0]
        cube[4][5][0] = cube[4][7][0]
        cube[4][7][0] = cube[4][3][0]
        cube[4][3][0] = swap_middle

    def rotate_cube(self, move):
        """ Rotate the cube by the move
        """
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
        """ Randomly shuffle the cube
        """
        sequence = ""
        for _ in range(number):
            choice = random.choice(["U", "D", "L", "R", "F", "B"])
            sequence += self.rotate_cube(choice)
        return sequence

    def sort_cube(self, listChoices):
        """ Sort the cube by the moves stored in list
        """
        # Reverse list before the iteration
        for choice in reversed(listChoices):
            self.rotate_cube_reverse(choice)
