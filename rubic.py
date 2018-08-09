# import sys
import pygame
from cube import Cube as CB

BLUE = [0, 0, 255]
YELLOW = [255, 255, 128]
ORANGE = [255, 105, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255,   0]
RED = [255,   0,   0]
BLACK = [0,   0,   0]

LEGEND = ["U - Move top clockwise", "D - Move bottom clockwise", "L - Move left side clockwise",
          "R - Move right side clockwise", "F - Move front side clockwise", "B - Move back side clockwise"]

Cube = CB()

def game_loop():
    pygame.init()
    Cube.init_cube()

    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption("Rubics Cube")
    pattern = False
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    # display text
    font = pygame.font.SysFont("comicsansms", 24)

    key_list = "Moves: "

    while not pattern:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pattern = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pattern = True
                if event.key == pygame.K_1:
                    Cube.init_cube()
                    key_list = "Moves: "
                key_list += key_pressed(event, pygame)

        screen.blit(background, (0, 0))

        draw_cube(pygame, screen)
        draw_text(screen, font, key_list)
        draw_legend(screen, font)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

def draw_cube(pygame, screen):
    """ Draw the cube on the screen
    """
    cube = Cube.get_cube()
    num_faces = Cube.get_num_faces()
    num_pieces_per_face = Cube.get_num_pieces_per_face()
    piece_size = Cube.get_piece_size()

    for side in range(num_faces):
        for row in range(num_pieces_per_face):
            draw_piece(pygame, screen, cube[side][row][0], [
                      cube[side][row][1], cube[side][row][2], piece_size, piece_size])

def draw_piece(pygame, screen, color, location):
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

def draw_text(screen, font, text):
    """ Render text on the screen
    """
    line = font.render(text, True, BLUE)
    screen.blit(line, (screen.get_width() - line.get_width() -
                       200, 200))

def draw_legend(screen, font):
    """ Render Legend on the screen
    """
    text_padding = 0
    for sentence in LEGEND:
        line = font.render(sentence, True, BLUE)
        screen.blit(line, (screen.get_width() - 400, 300 + text_padding))
        text_padding += 100

def key_pressed(event, pygame):
    if event.key == pygame.K_u:
        Cube.rotate_top()
        return "U"
    if event.key == pygame.K_d:
        Cube.rotate_bottom()
        return "D"
    if event.key == pygame.K_l:
        Cube.rotate_left()
        return "L"
    if event.key == pygame.K_r:
        Cube.rotate_right()
        return "R"
    if event.key == pygame.K_f:
        Cube.rotate_front()
        return "F"
    if event.key == pygame.K_b:
        Cube.rotate_back()
        return "B"
    if event.key == pygame.K_0:
        return Cube.random_shuffle(number=10)
    return ""


# Start game
game_loop()
