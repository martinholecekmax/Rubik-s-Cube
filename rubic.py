import random
import sys

import numpy as np
import pygame

pygame.init()

BLUE = [0, 0, 255]
YELLOW = [255, 255, 128]
ORANGE = [255, 105, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255,   0]
RED = [255,   0,   0]
BLACK = [0,   0,   0]

RECT_SIZE = 50
NUM_FACES = 6
NUM_PIECES_PER_FACE = 9
NUM_PIECES_PER_ROW = 3

CUBE_ARRAY = np.full(
    (NUM_FACES, NUM_PIECES_PER_FACE, NUM_PIECES_PER_ROW), 0)

LEGEND = ["U - Move top clockwise", "D - Move bottom clockwise", "L - Move left side clockwise",
          "R - Move right side clockwise", "F - Move front side clockwise", "B - Move back side clockwise"]


def drawPiece(color, location):
    """ Draw piece to the screen with color and location
        Colors: 0 - White, 1 - Green, 2 - Red, 3 - Blue, 4 - Orange, 5 - Yellow
    """
    if color == 0:
        pygame.draw.rect(screen, WHITE, location)
    elif color == 1:
        pygame.draw.rect(screen, GREEN, location)
    elif color == 2:
        pygame.draw.rect(screen, RED, location)
    elif color == 3:
        pygame.draw.rect(screen, BLUE, location)
    elif color == 4:
        pygame.draw.rect(screen, ORANGE, location)
    else:
        pygame.draw.rect(screen, YELLOW, location)
    pygame.draw.rect(screen, BLACK, location, 2)


def initCube(pieceSize):
    """ Initialize the cube
    """
    numFaces = NUM_FACES
    numPiecesPerFace = NUM_PIECES_PER_FACE
    numPiecesInRow = NUM_PIECES_PER_ROW

    posCol = pieceSize
    posRow = pieceSize
    posFaceCol = numPiecesInRow * pieceSize     # First face has one face offset
    posFaceRow = 0
    for side in range(numFaces):
        for row in range(numPiecesPerFace):
            for col in range(numPiecesInRow):
                if col == 0:
                    CUBE_ARRAY[side][row][col] = side
                    if posCol > numPiecesInRow * pieceSize:
                        posCol = pieceSize
                        posRow += pieceSize
                    if posRow > numPiecesInRow * pieceSize:
                        posRow = pieceSize
                elif col == 1:
                    CUBE_ARRAY[side][row][col] = posRow + posFaceCol
                else:
                    CUBE_ARRAY[side][row][col] = posCol + posFaceRow

                # last piece in row increment row
                if numPiecesInRow - 1 == col:
                    posCol += pieceSize
        posFaceCol += numPiecesInRow * pieceSize
        if side == 0:
            posFaceRow += numPiecesInRow * pieceSize
            posFaceCol = 0
            posCol = pieceSize
            posRow = pieceSize
        if side == 4:
            # Last face has one face offset in horizontal direction
            posFaceCol = numPiecesInRow * pieceSize
            # Last face has two face offset in vertical direction
            posFaceRow = 2 * numPiecesInRow * pieceSize
            posCol = pieceSize
            posRow = pieceSize


def rotateFront():
    """ Rotate Front face of a cube clockwise (F move to the right)
    """
    swap1 = CUBE_ARRAY[0][2][0]
    swap2 = CUBE_ARRAY[0][5][0]
    swap3 = CUBE_ARRAY[0][8][0]

    CUBE_ARRAY[0][2][0] = CUBE_ARRAY[1][8][0]
    CUBE_ARRAY[1][8][0] = CUBE_ARRAY[5][6][0]
    CUBE_ARRAY[5][6][0] = CUBE_ARRAY[3][0][0]
    CUBE_ARRAY[3][0][0] = swap1

    CUBE_ARRAY[0][5][0] = CUBE_ARRAY[1][7][0]
    CUBE_ARRAY[1][7][0] = CUBE_ARRAY[5][3][0]
    CUBE_ARRAY[5][3][0] = CUBE_ARRAY[3][1][0]
    CUBE_ARRAY[3][1][0] = swap2

    CUBE_ARRAY[0][8][0] = CUBE_ARRAY[1][6][0]
    CUBE_ARRAY[1][6][0] = CUBE_ARRAY[5][0][0]
    CUBE_ARRAY[5][0][0] = CUBE_ARRAY[3][2][0]
    CUBE_ARRAY[3][2][0] = swap3

    swapCorner = CUBE_ARRAY[2][0][0]
    CUBE_ARRAY[2][0][0] = CUBE_ARRAY[2][2][0]
    CUBE_ARRAY[2][2][0] = CUBE_ARRAY[2][8][0]
    CUBE_ARRAY[2][8][0] = CUBE_ARRAY[2][6][0]
    CUBE_ARRAY[2][6][0] = swapCorner

    swapMiddle = CUBE_ARRAY[2][1][0]
    CUBE_ARRAY[2][1][0] = CUBE_ARRAY[2][5][0]
    CUBE_ARRAY[2][5][0] = CUBE_ARRAY[2][7][0]
    CUBE_ARRAY[2][7][0] = CUBE_ARRAY[2][3][0]
    CUBE_ARRAY[2][3][0] = swapMiddle


def rotateBack():
    """ Rotate Back face of a cube clockwise (B move to the right)
    """
    swap1 = CUBE_ARRAY[0][0][0]
    swap2 = CUBE_ARRAY[0][3][0]
    swap3 = CUBE_ARRAY[0][6][0]

    CUBE_ARRAY[0][0][0] = CUBE_ARRAY[3][6][0]
    CUBE_ARRAY[3][6][0] = CUBE_ARRAY[5][8][0]
    CUBE_ARRAY[5][8][0] = CUBE_ARRAY[1][2][0]
    CUBE_ARRAY[1][2][0] = swap1

    CUBE_ARRAY[0][3][0] = CUBE_ARRAY[3][7][0]
    CUBE_ARRAY[3][7][0] = CUBE_ARRAY[5][5][0]
    CUBE_ARRAY[5][5][0] = CUBE_ARRAY[1][1][0]
    CUBE_ARRAY[1][1][0] = swap2

    CUBE_ARRAY[0][6][0] = CUBE_ARRAY[3][8][0]
    CUBE_ARRAY[3][8][0] = CUBE_ARRAY[5][2][0]
    CUBE_ARRAY[5][2][0] = CUBE_ARRAY[1][0][0]
    CUBE_ARRAY[1][0][0] = swap3

    swapCorner = CUBE_ARRAY[4][0][0]
    CUBE_ARRAY[4][0][0] = CUBE_ARRAY[4][2][0]
    CUBE_ARRAY[4][2][0] = CUBE_ARRAY[4][8][0]
    CUBE_ARRAY[4][8][0] = CUBE_ARRAY[4][6][0]
    CUBE_ARRAY[4][6][0] = swapCorner

    swapMiddle = CUBE_ARRAY[4][1][0]
    CUBE_ARRAY[4][1][0] = CUBE_ARRAY[4][5][0]
    CUBE_ARRAY[4][5][0] = CUBE_ARRAY[4][7][0]
    CUBE_ARRAY[4][7][0] = CUBE_ARRAY[4][3][0]
    CUBE_ARRAY[4][3][0] = swapMiddle


def rotateLeft():
    """ Rotate Left face of a cube clockwise (L move to the right)
    """
    swap1 = CUBE_ARRAY[4][6][0]
    swap2 = CUBE_ARRAY[4][7][0]
    swap3 = CUBE_ARRAY[4][8][0]

    CUBE_ARRAY[4][6][0] = CUBE_ARRAY[5][2][0]
    CUBE_ARRAY[5][2][0] = CUBE_ARRAY[2][2][0]
    CUBE_ARRAY[2][2][0] = CUBE_ARRAY[0][2][0]
    CUBE_ARRAY[0][2][0] = swap1

    CUBE_ARRAY[4][7][0] = CUBE_ARRAY[5][1][0]
    CUBE_ARRAY[5][1][0] = CUBE_ARRAY[2][1][0]
    CUBE_ARRAY[2][1][0] = CUBE_ARRAY[0][1][0]
    CUBE_ARRAY[0][1][0] = swap2

    CUBE_ARRAY[4][8][0] = CUBE_ARRAY[5][0][0]
    CUBE_ARRAY[5][0][0] = CUBE_ARRAY[2][0][0]
    CUBE_ARRAY[2][0][0] = CUBE_ARRAY[0][0][0]
    CUBE_ARRAY[0][0][0] = swap3

    swapCorner = CUBE_ARRAY[1][0][0]
    CUBE_ARRAY[1][0][0] = CUBE_ARRAY[1][2][0]
    CUBE_ARRAY[1][2][0] = CUBE_ARRAY[1][8][0]
    CUBE_ARRAY[1][8][0] = CUBE_ARRAY[1][6][0]
    CUBE_ARRAY[1][6][0] = swapCorner

    swapMiddle = CUBE_ARRAY[1][1][0]
    CUBE_ARRAY[1][1][0] = CUBE_ARRAY[1][5][0]
    CUBE_ARRAY[1][5][0] = CUBE_ARRAY[1][7][0]
    CUBE_ARRAY[1][7][0] = CUBE_ARRAY[1][3][0]
    CUBE_ARRAY[1][3][0] = swapMiddle


def rotateRight():
    """ Rotate Right face of a cube clockwise (R move to the right)
    """
    swap1 = CUBE_ARRAY[0][6][0]
    swap2 = CUBE_ARRAY[0][7][0]
    swap3 = CUBE_ARRAY[0][8][0]

    CUBE_ARRAY[0][6][0] = CUBE_ARRAY[2][6][0]
    CUBE_ARRAY[2][6][0] = CUBE_ARRAY[5][6][0]
    CUBE_ARRAY[5][6][0] = CUBE_ARRAY[4][2][0]
    CUBE_ARRAY[4][2][0] = swap1

    CUBE_ARRAY[0][7][0] = CUBE_ARRAY[2][7][0]
    CUBE_ARRAY[2][7][0] = CUBE_ARRAY[5][7][0]
    CUBE_ARRAY[5][7][0] = CUBE_ARRAY[4][1][0]
    CUBE_ARRAY[4][1][0] = swap2

    CUBE_ARRAY[0][8][0] = CUBE_ARRAY[2][8][0]
    CUBE_ARRAY[2][8][0] = CUBE_ARRAY[5][8][0]
    CUBE_ARRAY[5][8][0] = CUBE_ARRAY[4][0][0]
    CUBE_ARRAY[4][0][0] = swap3

    swapCorner = CUBE_ARRAY[3][0][0]
    CUBE_ARRAY[3][0][0] = CUBE_ARRAY[3][2][0]
    CUBE_ARRAY[3][2][0] = CUBE_ARRAY[3][8][0]
    CUBE_ARRAY[3][8][0] = CUBE_ARRAY[3][6][0]
    CUBE_ARRAY[3][6][0] = swapCorner

    swapMiddle = CUBE_ARRAY[3][1][0]
    CUBE_ARRAY[3][1][0] = CUBE_ARRAY[3][5][0]
    CUBE_ARRAY[3][5][0] = CUBE_ARRAY[3][7][0]
    CUBE_ARRAY[3][7][0] = CUBE_ARRAY[3][3][0]
    CUBE_ARRAY[3][3][0] = swapMiddle


def rotateTop():
    """ Rotate Top face of a cube clockwise (U move to the right)
    """
    swap1 = CUBE_ARRAY[1][0][0]
    swap2 = CUBE_ARRAY[1][3][0]
    swap3 = CUBE_ARRAY[1][6][0]

    CUBE_ARRAY[1][0][0] = CUBE_ARRAY[2][0][0]
    CUBE_ARRAY[2][0][0] = CUBE_ARRAY[3][0][0]
    CUBE_ARRAY[3][0][0] = CUBE_ARRAY[4][0][0]
    CUBE_ARRAY[4][0][0] = swap1

    CUBE_ARRAY[1][3][0] = CUBE_ARRAY[2][3][0]
    CUBE_ARRAY[2][3][0] = CUBE_ARRAY[3][3][0]
    CUBE_ARRAY[3][3][0] = CUBE_ARRAY[4][3][0]
    CUBE_ARRAY[4][3][0] = swap2

    CUBE_ARRAY[1][6][0] = CUBE_ARRAY[2][6][0]
    CUBE_ARRAY[2][6][0] = CUBE_ARRAY[3][6][0]
    CUBE_ARRAY[3][6][0] = CUBE_ARRAY[4][6][0]
    CUBE_ARRAY[4][6][0] = swap3

    swapCorner = CUBE_ARRAY[0][0][0]
    CUBE_ARRAY[0][0][0] = CUBE_ARRAY[0][2][0]
    CUBE_ARRAY[0][2][0] = CUBE_ARRAY[0][8][0]
    CUBE_ARRAY[0][8][0] = CUBE_ARRAY[0][6][0]
    CUBE_ARRAY[0][6][0] = swapCorner

    swapMiddle = CUBE_ARRAY[0][1][0]
    CUBE_ARRAY[0][1][0] = CUBE_ARRAY[0][5][0]
    CUBE_ARRAY[0][5][0] = CUBE_ARRAY[0][7][0]
    CUBE_ARRAY[0][7][0] = CUBE_ARRAY[0][3][0]
    CUBE_ARRAY[0][3][0] = swapMiddle


def rotateBottom():
    """ Rotate Bottom face of a cube clockwise (D move to the right)
    """
    swap1 = CUBE_ARRAY[1][2][0]
    swap2 = CUBE_ARRAY[1][5][0]
    swap3 = CUBE_ARRAY[1][8][0]

    CUBE_ARRAY[1][2][0] = CUBE_ARRAY[4][2][0]
    CUBE_ARRAY[4][2][0] = CUBE_ARRAY[3][2][0]
    CUBE_ARRAY[3][2][0] = CUBE_ARRAY[2][2][0]
    CUBE_ARRAY[2][2][0] = swap1

    CUBE_ARRAY[1][5][0] = CUBE_ARRAY[4][5][0]
    CUBE_ARRAY[4][5][0] = CUBE_ARRAY[3][5][0]
    CUBE_ARRAY[3][5][0] = CUBE_ARRAY[2][5][0]
    CUBE_ARRAY[2][5][0] = swap2

    CUBE_ARRAY[1][8][0] = CUBE_ARRAY[4][8][0]
    CUBE_ARRAY[4][8][0] = CUBE_ARRAY[3][8][0]
    CUBE_ARRAY[3][8][0] = CUBE_ARRAY[2][8][0]
    CUBE_ARRAY[2][8][0] = swap3

    swapCorner = CUBE_ARRAY[5][0][0]
    CUBE_ARRAY[5][0][0] = CUBE_ARRAY[5][2][0]
    CUBE_ARRAY[5][2][0] = CUBE_ARRAY[5][8][0]
    CUBE_ARRAY[5][8][0] = CUBE_ARRAY[5][6][0]
    CUBE_ARRAY[5][6][0] = swapCorner

    swapMiddle = CUBE_ARRAY[5][1][0]
    CUBE_ARRAY[5][1][0] = CUBE_ARRAY[5][5][0]
    CUBE_ARRAY[5][5][0] = CUBE_ARRAY[5][7][0]
    CUBE_ARRAY[5][7][0] = CUBE_ARRAY[5][3][0]
    CUBE_ARRAY[5][3][0] = swapMiddle


def randomShuffle(number):
    """ Randomly shuffle the cube
    """
    sequence = ""
    for _ in range(number):
        choice = random.choice(["U", "D", "L", "R", "F", "B"])
        sequence += rotateCube(choice)
    return sequence


def sortCube(listChoices):
    """ Sort the cube by the moves stored in list
    """
    # Reverse list before the iteration
    for choice in reversed(listChoices):
        for _ in range(3):
            rotateCube(choice)


def rotateCube(move):
    """ Rotate the cube by the move
    """
    if move == "U":
        rotateTop()
        return "U"
    elif move == "D":
        rotateBottom()
        return "D"
    elif move == "L":
        rotateLeft()
        return "L"
    elif move == "R":
        rotateRight()
        return "R"
    elif move == "F":
        rotateFront()
        return "F"
    else:
        rotateBack()
        return "B"


def drawCube():
    """ Draw the cube on the screen
    """
    for side in range(NUM_FACES):
        for row in range(NUM_PIECES_PER_FACE):
            drawPiece(CUBE_ARRAY[side][row][0], [
                      CUBE_ARRAY[side][row][1], CUBE_ARRAY[side][row][2], RECT_SIZE, RECT_SIZE])


def drawText(screen, font, text):
    """ Render text on the screen
    """
    line = font.render(text, True, BLUE)
    screen.blit(line, (screen.get_width() - line.get_width() -
                       200, 200))


def drawLegend(screen, font):
    """ Render Legend on the screen
    """
    textPadding = 0
    for sentence in LEGEND:
        line = font.render(sentence, True, BLUE)
        screen.blit(line, (screen.get_width() - 400, 300 + textPadding))
        textPadding += 100


initCube(RECT_SIZE)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Rubics Cube")
pattern = False
clock = pygame.time.Clock()

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

# display text
font = pygame.font.SysFont("comicsansms", 24)

key = "Moves: "

listOfMoves = []

while not pattern:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pattern = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pattern = True
            if event.key == pygame.K_u:
                rotateTop()
                key += "U "
            if event.key == pygame.K_d:
                rotateBottom()
                key += "D "
            if event.key == pygame.K_l:
                rotateLeft()
                key += "L "
            if event.key == pygame.K_r:
                rotateRight()
                key += "R "
            if event.key == pygame.K_f:
                rotateFront()
                key += "F "
            if event.key == pygame.K_b:
                rotateBack()
                key += "B "

            # press 0 to shuffle cube
            if event.key == pygame.K_0:
                # Shuffle - make 1000 random moves
                sh = randomShuffle(1000)

                # Write shuffle algorithm into the file
                # with open("text2", "w") as f:
                #     f.write(sh)

                # Insert shuffle into the list
                listOfMoves.clear()
                for a in sh:
                    listOfMoves.append(a)
            # press 1 to sort a cube
            if event.key == pygame.K_1:
                sortCube(listOfMoves)

    screen.blit(background, (0, 0))

    drawCube()
    drawText(screen, font, key)
    drawLegend(screen, font)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
