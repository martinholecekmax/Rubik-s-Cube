BLUE_BGR = [255, 0, 0]
YELLOW_BGR = [128, 255, 255]
ORANGE_BGR = [0, 105, 255]
WHITE_BGR = [255, 255, 255]
GREEN_BGR = [0, 255,   0]
RED_BGR = [0,   0,   255]
BLACK_BGR = [0,   0,   0]

BLUE_RGB = [0, 0, 255]
YELLOW_RGB = [255, 255, 128]
ORANGE_RGB = [255, 105, 0]
WHITE_RGB = [255, 255, 255]
GREEN_RGB = [0, 255,   0]
RED_RGB = [255,   0,   0]
BLACK_RGB = [0,   0,   0]

WHITE_GL_RGB = [1, 1, 1]
GREEN_GL_RGB = [0, 1,   0]
RED_GL_RGB = [1,   0,   0]
BLUE_GL_RGB = [0, 0, 1]
ORANGE_GL_RGB = [1, 0.5, 0]
YELLOW_GL_RGB = [1, 1, 0]
BLACK_GL_RGB = [0,   0,   0]


def get_color_BGR(color):
    """ Colors: 0 - White, 1 - Green, 2 - Red, 3 - Blue, 4 - Orange, 5 - Yellow """
    if color == 0:
        return WHITE_BGR
    elif color == 1:
        return GREEN_BGR
    elif color == 2:
        return RED_BGR
    elif color == 3:
        return BLUE_BGR
    elif color == 4:
        return ORANGE_BGR
    else:
        return YELLOW_BGR


def get_color_GL_RGB(color):
    """ Colors: 0 - White, 1 - Green, 2 - Red, 3 - Blue, 4 - Orange, 5 - Yellow """
    if color == 0:
        return WHITE_GL_RGB
    elif color == 1:
        return GREEN_GL_RGB
    elif color == 2:
        return RED_GL_RGB
    elif color == 3:
        return BLUE_GL_RGB
    elif color == 4:
        return ORANGE_GL_RGB
    elif color == 5:
        return YELLOW_GL_RGB
    else:
        return BLACK_GL_RGB
