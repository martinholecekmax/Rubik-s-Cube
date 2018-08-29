import numpy as np
import color as Color
from pyglet.gl import *


class CubePiece:
    def draw_piece(self, x, y, width, height, color):
        """
            draw_rec( x , y , width , height , color )
            :param x: x location
            :param y: y location
            :param width: width
            :param height: height
            :param color: color
        """
        # Draw filled the rectangle
        glColor3f(color[0], color[1], color[2])
        glBegin(GL_QUADS)
        glVertex2f(x, y)                    # bottom left point
        glVertex2f(x + width, y)            # bottom right point
        glVertex2f(x + width, y + height)   # top right point
        glVertex2f(x, y + height)            # top right point
        glEnd()

        # Draw lines around the rectangle
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x, y)
        glVertex2f(x + width + 1, y)    # the number one is the line thickness
        glVertex2f(x + width, y + height)
        glVertex2f(x, y + height)
        glEnd()

    def refresh_2D(self, width, height):
        """
            Convert gl coordinates into screen coordinates

                refresh2d(self.Rectangle, width, height)
                :param width: window width
                :param height: window height

            To switch coordinates transformation to (0, 0)
            coordinates located at bottom, left corner
            use this function:

                glOrtho(0.0, width, 0.0, height, 0.0, 1.0)

            default coordinates (0, 0) are at top, left corner
            which defines this function:

                glOrtho(0.0, width, height, 0.0, -1.0, 1.0)
        """
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, width, height, 0.0, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


class View:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.winname = "Rubics Cube"
        self.window = pyglet.window.Window(
            width, height, self.winname, resizable=True)
        self.isopen = True
        self.window.on_close = self.window_closed_by_user
        self.piece = CubePiece()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def close(self):
        self.window.close()

    def window_closed_by_user(self):
        self.isopen = False

    def render(self, colors):
        glClearColor(1, 1, 1, 1)
        self.window.clear()
        self.draw_cube(colors)
        self.window.switch_to()
        self.window.dispatch_events()
        self.window.flip()
        return self.isopen

    def draw_cube(self, colors):
        piece_size = 50
        self.piece.refresh_2D(self.width, self.height)
        cube_position = self.init_cube_position()
        for side in range(6):
            for row in range(3):
                for col in range(3):
                    self.piece.draw_piece(
                        cube_position[side][row][col][0], cube_position[side][row][col][1], piece_size, piece_size, Color.get_color_GL_RGB(colors[side][row][col]))

    def init_cube_position(self):
        """ Initialize positions of each piece of the cube """
        num_faces = 6
        num_pieces_per_face = 9
        num_pieces_per_row = 3
        num_pieces_per_col = 3
        cube_position = np.full((num_faces, num_pieces_per_row,
                                 num_pieces_per_col, 2), 0)
        piece_size = 50
        column_position = piece_size
        row_position = piece_size
        face_column_position = num_pieces_per_col * \
            piece_size     # First face has one face offset
        face_row_position = 0

        for side in range(num_faces):
            for row in range(num_pieces_per_row):
                for col in range(num_pieces_per_col):
                    cube_position[side][row][col][0] = column_position + \
                        face_column_position
                    cube_position[side][row][col][1] = row_position + \
                        face_row_position
                    column_position += piece_size
                row_position += piece_size
                column_position = piece_size
            row_position = piece_size
            column_position = piece_size
            face_column_position += num_pieces_per_col * piece_size
            if side == 0:
                face_row_position += num_pieces_per_row * \
                    piece_size    # face offset in horizontal direction
                face_column_position = 0
            if side == 4:
                face_column_position = num_pieces_per_col * \
                    piece_size  # face offset in horizontal direction
                face_row_position += num_pieces_per_row * \
                    piece_size    # face offset in vertical direction
        return cube_position
