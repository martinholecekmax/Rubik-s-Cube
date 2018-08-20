import cv2
import numpy as np
import screeninfo
import color as Color


class View:
    def __init__(self):
        self.screen_id = 0
        self.screen = screeninfo.get_monitors()[self.screen_id]
        self.width, self.height = self.screen.width, self.screen.height
        self.winname = "Rubics Cube"
        cv2.namedWindow(self.winname)        # Create a named window
        cv2.moveWindow(self.winname, 0, 0)

    def render(self, color):
        img = np.full((self.height, self.width, 3), 255, np.uint8)
        self.draw_cube(color, img)
        cv2.imwrite('cube.png', img)
        cv2.imshow(self.winname, img)
        cv2.waitKey(0)

    def draw_cube(self, color, img):
        color_filled = 1
        piece_size = 50
        position_cube_x = 200
        position_cube_y = 200
        pos_col = position_cube_x
        pos_row = position_cube_y
        face_row = 0
        face_column = 3 * piece_size
        for face in range(6):
            for row in range(3):
                for col in range(3):
                    position_x = pos_col + face_column
                    position_y = pos_row + face_row
                    cv2.rectangle(img, (position_x, position_y),
                                  (position_x + piece_size, position_y + piece_size), Color.get_color(color[face][row][col]), -1)
                    cv2.rectangle(img, (position_x, position_y),
                                  (position_x + piece_size, position_y + piece_size), Color.BLACK, color_filled)
                    pos_col = pos_col + piece_size
                pos_col = position_cube_x
                pos_row = pos_row + piece_size
            pos_row = position_cube_y
            pos_col = position_cube_x
            if face == 0:
                face_row = face_row + 3 * piece_size
                face_column = 0
            elif face == 4:
                face_row = face_row + 3 * piece_size
                face_column = 3 * piece_size
            else:
                face_column += 3 * piece_size

    def close(self):
        cv2.destroyAllWindows()
