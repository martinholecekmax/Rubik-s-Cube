import pygame
import numpy as np
import sys
import random

pygame.init()

BLUE = [0, 0, 255]
YELLOW = [255, 255, 128]
ORANGE = [255, 105, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255,   0]
RED = [255,   0,   0]
BLACK = [0,   0,   0]

RECT_SIZE = 100
UNITS_POSITION = np.full((6, 9, 3), 0)
LEGEND = ["U - Move top clockwise", "D - Move bottom clockwise", "L - Move left side clockwise",
          "R - Move right side clockwise", "F - Move front side clockwise", "B - Move back side clockwise"]

# Draw piece to the screen, Colors: 0 - White, 1 - Green, 2 - Red, 3 - Blue, 4 - Orange, 5 - Yellow


def drawPiece(color, location):
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
    numFaces = 6
    numPiecesPerFace = 9
    numPiecesInRow = 3

    posCol = pieceSize
    posRow = pieceSize
    posSideCol = 3 * pieceSize
    posSideRow = 0
    for side in range(numFaces):
        for row in range(numPicesPerFace):
            for col in range(numPiecesInRow):
                if col == 0:
                    UNITS_POSITION[side][row][col] = side
                    if posCol > 3 * pieceSize:
                        posCol = pieceSize
                        posRow += pieceSize
                    if posRow > 3 * pieceSize:
                        posRow = pieceSize
                elif col == 2:
                    UNITS_POSITION[side][row][col] = posCol + posSideRow
                    posCol += pieceSize
                else:
                    UNITS_POSITION[side][row][col] = posRow + posSideCol
        posSideCol += 3 * pieceSize
        if side == 0:
            posSideRow += 3 * pieceSize
            posSideCol = 0
            posCol = pieceSize
            posRow = pieceSize
        if side == 4:
            posSideCol = 3 * pieceSize
            posSideRow = 6 * pieceSize
            posCol = pieceSize
            posRow = pieceSize


def rotateFront():
    swap1 = UNITS_POSITION[0][2][0]
    swap2 = UNITS_POSITION[0][5][0]
    swap3 = UNITS_POSITION[0][8][0]

    UNITS_POSITION[0][2][0] = UNITS_POSITION[1][8][0]
    UNITS_POSITION[1][8][0] = UNITS_POSITION[5][6][0]
    UNITS_POSITION[5][6][0] = UNITS_POSITION[3][0][0]
    UNITS_POSITION[3][0][0] = swap1

    UNITS_POSITION[0][5][0] = UNITS_POSITION[1][7][0]
    UNITS_POSITION[1][7][0] = UNITS_POSITION[5][3][0]
    UNITS_POSITION[5][3][0] = UNITS_POSITION[3][1][0]
    UNITS_POSITION[3][1][0] = swap2

    UNITS_POSITION[0][8][0] = UNITS_POSITION[1][6][0]
    UNITS_POSITION[1][6][0] = UNITS_POSITION[5][0][0]
    UNITS_POSITION[5][0][0] = UNITS_POSITION[3][2][0]
    UNITS_POSITION[3][2][0] = swap3

    swapCorner = UNITS_POSITION[2][0][0]
    UNITS_POSITION[2][0][0] = UNITS_POSITION[2][2][0]
    UNITS_POSITION[2][2][0] = UNITS_POSITION[2][8][0]
    UNITS_POSITION[2][8][0] = UNITS_POSITION[2][6][0]
    UNITS_POSITION[2][6][0] = swapCorner

    swapMiddle = UNITS_POSITION[2][1][0]
    UNITS_POSITION[2][1][0] = UNITS_POSITION[2][5][0]
    UNITS_POSITION[2][5][0] = UNITS_POSITION[2][7][0]
    UNITS_POSITION[2][7][0] = UNITS_POSITION[2][3][0]
    UNITS_POSITION[2][3][0] = swapMiddle


def rotateBack():
    swap1 = UNITS_POSITION[0][0][0]
    swap2 = UNITS_POSITION[0][3][0]
    swap3 = UNITS_POSITION[0][6][0]

    UNITS_POSITION[0][0][0] = UNITS_POSITION[3][6][0]
    UNITS_POSITION[3][6][0] = UNITS_POSITION[5][8][0]
    UNITS_POSITION[5][8][0] = UNITS_POSITION[1][2][0]
    UNITS_POSITION[1][2][0] = swap1

    UNITS_POSITION[0][3][0] = UNITS_POSITION[3][7][0]
    UNITS_POSITION[3][7][0] = UNITS_POSITION[5][5][0]
    UNITS_POSITION[5][5][0] = UNITS_POSITION[1][1][0]
    UNITS_POSITION[1][1][0] = swap2

    UNITS_POSITION[0][6][0] = UNITS_POSITION[3][8][0]
    UNITS_POSITION[3][8][0] = UNITS_POSITION[5][2][0]
    UNITS_POSITION[5][2][0] = UNITS_POSITION[1][0][0]
    UNITS_POSITION[1][0][0] = swap3

    swapCorner = UNITS_POSITION[4][0][0]
    UNITS_POSITION[4][0][0] = UNITS_POSITION[4][2][0]
    UNITS_POSITION[4][2][0] = UNITS_POSITION[4][8][0]
    UNITS_POSITION[4][8][0] = UNITS_POSITION[4][6][0]
    UNITS_POSITION[4][6][0] = swapCorner

    swapMiddle = UNITS_POSITION[4][1][0]
    UNITS_POSITION[4][1][0] = UNITS_POSITION[4][5][0]
    UNITS_POSITION[4][5][0] = UNITS_POSITION[4][7][0]
    UNITS_POSITION[4][7][0] = UNITS_POSITION[4][3][0]
    UNITS_POSITION[4][3][0] = swapMiddle


def rotateLeft():
    swap1 = UNITS_POSITION[4][6][0]
    swap2 = UNITS_POSITION[4][7][0]
    swap3 = UNITS_POSITION[4][8][0]

    UNITS_POSITION[4][6][0] = UNITS_POSITION[5][2][0]
    UNITS_POSITION[5][2][0] = UNITS_POSITION[2][2][0]
    UNITS_POSITION[2][2][0] = UNITS_POSITION[0][2][0]
    UNITS_POSITION[0][2][0] = swap1

    UNITS_POSITION[4][7][0] = UNITS_POSITION[5][1][0]
    UNITS_POSITION[5][1][0] = UNITS_POSITION[2][1][0]
    UNITS_POSITION[2][1][0] = UNITS_POSITION[0][1][0]
    UNITS_POSITION[0][1][0] = swap2

    UNITS_POSITION[4][8][0] = UNITS_POSITION[5][0][0]
    UNITS_POSITION[5][0][0] = UNITS_POSITION[2][0][0]
    UNITS_POSITION[2][0][0] = UNITS_POSITION[0][0][0]
    UNITS_POSITION[0][0][0] = swap3

    swapCorner = UNITS_POSITION[1][0][0]
    UNITS_POSITION[1][0][0] = UNITS_POSITION[1][2][0]
    UNITS_POSITION[1][2][0] = UNITS_POSITION[1][8][0]
    UNITS_POSITION[1][8][0] = UNITS_POSITION[1][6][0]
    UNITS_POSITION[1][6][0] = swapCorner

    swapMiddle = UNITS_POSITION[1][1][0]
    UNITS_POSITION[1][1][0] = UNITS_POSITION[1][5][0]
    UNITS_POSITION[1][5][0] = UNITS_POSITION[1][7][0]
    UNITS_POSITION[1][7][0] = UNITS_POSITION[1][3][0]
    UNITS_POSITION[1][3][0] = swapMiddle


def rotateRightSide():
    swap1 = UNITS_POSITION[0][6][0]
    swap2 = UNITS_POSITION[0][7][0]
    swap3 = UNITS_POSITION[0][8][0]

    UNITS_POSITION[0][6][0] = UNITS_POSITION[2][6][0]
    UNITS_POSITION[2][6][0] = UNITS_POSITION[5][6][0]
    UNITS_POSITION[5][6][0] = UNITS_POSITION[4][2][0]
    UNITS_POSITION[4][2][0] = swap1

    UNITS_POSITION[0][7][0] = UNITS_POSITION[2][7][0]
    UNITS_POSITION[2][7][0] = UNITS_POSITION[5][7][0]
    UNITS_POSITION[5][7][0] = UNITS_POSITION[4][1][0]
    UNITS_POSITION[4][1][0] = swap2

    UNITS_POSITION[0][8][0] = UNITS_POSITION[2][8][0]
    UNITS_POSITION[2][8][0] = UNITS_POSITION[5][8][0]
    UNITS_POSITION[5][8][0] = UNITS_POSITION[4][0][0]
    UNITS_POSITION[4][0][0] = swap3

    swapCorner = UNITS_POSITION[3][0][0]
    UNITS_POSITION[3][0][0] = UNITS_POSITION[3][2][0]
    UNITS_POSITION[3][2][0] = UNITS_POSITION[3][8][0]
    UNITS_POSITION[3][8][0] = UNITS_POSITION[3][6][0]
    UNITS_POSITION[3][6][0] = swapCorner

    swapMiddle = UNITS_POSITION[3][1][0]
    UNITS_POSITION[3][1][0] = UNITS_POSITION[3][5][0]
    UNITS_POSITION[3][5][0] = UNITS_POSITION[3][7][0]
    UNITS_POSITION[3][7][0] = UNITS_POSITION[3][3][0]
    UNITS_POSITION[3][3][0] = swapMiddle


def rotateTop():
    swap1 = UNITS_POSITION[1][0][0]
    swap2 = UNITS_POSITION[1][3][0]
    swap3 = UNITS_POSITION[1][6][0]

    UNITS_POSITION[1][0][0] = UNITS_POSITION[2][0][0]
    UNITS_POSITION[2][0][0] = UNITS_POSITION[3][0][0]
    UNITS_POSITION[3][0][0] = UNITS_POSITION[4][0][0]
    UNITS_POSITION[4][0][0] = swap1

    UNITS_POSITION[1][3][0] = UNITS_POSITION[2][3][0]
    UNITS_POSITION[2][3][0] = UNITS_POSITION[3][3][0]
    UNITS_POSITION[3][3][0] = UNITS_POSITION[4][3][0]
    UNITS_POSITION[4][3][0] = swap2

    UNITS_POSITION[1][6][0] = UNITS_POSITION[2][6][0]
    UNITS_POSITION[2][6][0] = UNITS_POSITION[3][6][0]
    UNITS_POSITION[3][6][0] = UNITS_POSITION[4][6][0]
    UNITS_POSITION[4][6][0] = swap3

    swapCorner = UNITS_POSITION[0][0][0]
    UNITS_POSITION[0][0][0] = UNITS_POSITION[0][2][0]
    UNITS_POSITION[0][2][0] = UNITS_POSITION[0][8][0]
    UNITS_POSITION[0][8][0] = UNITS_POSITION[0][6][0]
    UNITS_POSITION[0][6][0] = swapCorner

    swapMiddle = UNITS_POSITION[0][1][0]
    UNITS_POSITION[0][1][0] = UNITS_POSITION[0][5][0]
    UNITS_POSITION[0][5][0] = UNITS_POSITION[0][7][0]
    UNITS_POSITION[0][7][0] = UNITS_POSITION[0][3][0]
    UNITS_POSITION[0][3][0] = swapMiddle


def rotateBottom():
    swap1 = UNITS_POSITION[1][2][0]
    swap2 = UNITS_POSITION[1][5][0]
    swap3 = UNITS_POSITION[1][8][0]

    UNITS_POSITION[1][2][0] = UNITS_POSITION[4][2][0]
    UNITS_POSITION[4][2][0] = UNITS_POSITION[3][2][0]
    UNITS_POSITION[3][2][0] = UNITS_POSITION[2][2][0]
    UNITS_POSITION[2][2][0] = swap1

    UNITS_POSITION[1][5][0] = UNITS_POSITION[4][5][0]
    UNITS_POSITION[4][5][0] = UNITS_POSITION[3][5][0]
    UNITS_POSITION[3][5][0] = UNITS_POSITION[2][5][0]
    UNITS_POSITION[2][5][0] = swap2

    UNITS_POSITION[1][8][0] = UNITS_POSITION[4][8][0]
    UNITS_POSITION[4][8][0] = UNITS_POSITION[3][8][0]
    UNITS_POSITION[3][8][0] = UNITS_POSITION[2][8][0]
    UNITS_POSITION[2][8][0] = swap3

    swapCorner = UNITS_POSITION[5][0][0]
    UNITS_POSITION[5][0][0] = UNITS_POSITION[5][2][0]
    UNITS_POSITION[5][2][0] = UNITS_POSITION[5][8][0]
    UNITS_POSITION[5][8][0] = UNITS_POSITION[5][6][0]
    UNITS_POSITION[5][6][0] = swapCorner

    swapMiddle = UNITS_POSITION[5][1][0]
    UNITS_POSITION[5][1][0] = UNITS_POSITION[5][5][0]
    UNITS_POSITION[5][5][0] = UNITS_POSITION[5][7][0]
    UNITS_POSITION[5][7][0] = UNITS_POSITION[5][3][0]
    UNITS_POSITION[5][3][0] = swapMiddle


def randomShuffle(number):
    sequence = ""
    for i in range(number):
        choice = random.choice(["U", "D", "L", "R", "F", "B"])
        sequence += rotateCube(choice)
    return sequence


def unshuffle(listChoices):
    for choice in reversed(listChoices):
        for i in range(3):
            rotateCube(choice)


def rotateCube(move):
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
        rotateRightSide()
        return "R"
    elif move == "F":
        rotateFront()
        return "F"
    else:
        rotateBack()
        return "B"


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

# shuffle()
listA = []

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
                rotateRightSide()
                key += "R "
            if event.key == pygame.K_f:
                rotateFront()
                key += "F "
            if event.key == pygame.K_b:
                rotateBack()
                key += "B "
            if event.key == pygame.K_0:
                # initCube(RECT_SIZE)
                sh = randomShuffle(1000)

                # Write shuffle algorithm into the file
                # with open("text2", "w") as f:
                #     f.write(sh)

                # Insert shuffle into the list
                listA.clear()
                for a in sh:
                    listA.append(a)

                print(listA)
                key = "Shuffled: "
            if event.key == pygame.K_1:
                unshuffle(listA)
                key = "Unshuffled: "

    screen.blit(background, (0, 0))

    for side in range(6):
        for row in range(9):
            drawPiece(UNITS_POSITION[side][row][0], [UNITS_POSITION[side][row][1],
                                                     UNITS_POSITION[side][row][2], RECT_SIZE, RECT_SIZE])

    # render text
    # screen.blit(text,
    #             (520 - text.get_width() // 2, 240 - text.get_height() // 2))
    # screen.blit(text,
    #             ((screen.get_width() - text.get_width()) // 2, (screen.get_height() - text.get_height()) // 2))
    text = font.render(key, True, BLUE)
    screen.blit(text, (screen.get_width() - text.get_width() -
                       200, 200))

    padding = 0
    for sentence in LEGEND:
        line = font.render(sentence, True, BLUE)
        screen.blit(line, (screen.get_width() - 400, 300 + padding))
        padding += 100

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
