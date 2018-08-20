BLUE = [255, 0, 0]
YELLOW = [128, 255, 255]
ORANGE = [0, 105, 255]
WHITE = [255, 255, 255]
GREEN = [0, 255,   0]
RED = [0,   0,   255]
BLACK = [0,   0,   0]

BLUE_RGB = [0, 0, 255]
YELLOW_RGB = [255, 255, 128]
ORANGE_RGB = [255, 105, 0]
WHITE_RGB = [255, 255, 255]
GREEN_RGB = [0, 255,   0]
RED_RGB = [255,   0,   0]
BLACK_RGB = [0,   0,   0]


def get_color(color):
    """ Colors: 0 - White, 1 - Green, 2 - Red, 3 - Blue, 4 - Orange, 5 - Yellow """
    if color == 0:
        return WHITE
    elif color == 1:
        return GREEN
    elif color == 2:
        return RED
    elif color == 3:
        return BLUE
    elif color == 4:
        return ORANGE
    else:
        return YELLOW
