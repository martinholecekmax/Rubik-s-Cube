import pygame
import cube as CB

BLUE = [0, 0, 255]
YELLOW = [255, 255, 128]
ORANGE = [255, 105, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255,   0]
RED = [255,   0,   0]
BLACK = [0,   0,   0]

LEGEND = ["U - Move top clockwise", "D - Move bottom clockwise", "L - Move left side clockwise",
          "R - Move right side clockwise", "F - Move front side clockwise", "B - Move back side clockwise", "Hold SHIFT key to move anti-clockwise"]

Cube = CB.Cube()

def game_loop():
    pygame.init()
    Cube.init_cube()

    print(Cube.cube_array)

    # Switch to fullscreen mode
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1500, 1000))

    pygame.display.set_caption("Rubics Cube")
    pattern = False
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    # Set Font
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
                       300, 200))

def draw_legend(screen, font):
    """ Render Legend on the screen
    """
    text_padding = 0
    for sentence in LEGEND:
        line = font.render(sentence, True, BLUE)
        screen.blit(line, (screen.get_width() - 500, 300 + text_padding))
        text_padding += 100

def key_pressed(event, pygame):
    if event.key == pygame.K_u and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        Cube.rotate_cube_reverse("U")
        return "U'"
    if event.key == pygame.K_u:
        Cube.rotate_cube("U")
        return "U"
    if event.key == pygame.K_d and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        Cube.rotate_cube_reverse("D")
        return "D'"
    if event.key == pygame.K_d:
        Cube.rotate_cube("D")
        return "D"
    if event.key == pygame.K_l and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        Cube.rotate_cube_reverse("L")
        return "L'"
    if event.key == pygame.K_l:
        Cube.rotate_cube("L")
        return "L"
    if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        Cube.rotate_cube_reverse("R")
        return "R'"
    if event.key == pygame.K_r:
        Cube.rotate_cube("R")
        return "R"
    if event.key == pygame.K_f and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        Cube.rotate_cube_reverse("F")
        return "F'"
    if event.key == pygame.K_f:
        Cube.rotate_cube("F")
        return "F"
    if event.key == pygame.K_b and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        Cube.rotate_cube_reverse("B")
        return "B'"
    if event.key == pygame.K_b:
        Cube.rotate_cube("B")
        return "B"
    if event.key == pygame.K_0:
        return Cube.random_shuffle(number=10)
    return ""

# Start game
game_loop()
