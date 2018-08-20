import pygame
import color as Color
import numpy as np

LEGEND = ["U - Move top clockwise", "D - Move bottom clockwise", "L - Move left side clockwise",
          "R - Move right side clockwise", "F - Move front side clockwise", "B - Move back side clockwise", "Hold SHIFT key to move anti-clockwise"]

def play(env):
    cube_position = np.full((env.get_num_faces(), env.get_num_pieces_per_row(), env.get_num_pieces_per_col(), env.get_position_array_row_size()), 0)
    pygame.init()
    env.reset()
    init_cube_position(env, cube_position)

    # Switch to fullscreen mode
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1500, 1000))
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    pygame.display.set_caption("Rubics Cube")
    pattern = False
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(Color.WHITE_RGB)

    # Set Font
    font = pygame.font.SysFont("comicsansms", 24)

    times_solved = 0

    while not pattern:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pattern = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pattern = True
                if event.key == pygame.K_1:
                    env.init_colors()
                key = key_pressed(env, event, pygame)
                if key != "X":
                    if env.is_solved():
                        times_solved = times_solved + 1
                        env.reset()

        screen.blit(background, (0, 0))     # clear screen

        draw_cube(env, pygame, screen, cube_position)
        draw_multiple_lines(screen, font, LEGEND,
                            screen_width - 100, 150, "RIGHT", 50)
        draw_text(screen, font, "Time solved: " + str(times_solved),
                  screen_width - 100, 50, "RIGHT")

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


def draw_cube(env, pygame, screen, cube_position):
    """ Draw the cube on the screen """
    cube_color = env.get_cube_colors()
    num_faces = env.get_num_faces()
    num_pieces_per_face = env.get_num_pieces_per_face()
    num_pieces_per_row = env.get_num_pieces_per_row()
    num_pieces_per_col = env.get_num_pieces_per_col()
    piece_size = env.get_piece_size()

    for side in range(num_faces):
        for row in range(num_pieces_per_row):
            for col in range(num_pieces_per_col):
                draw_piece(pygame, screen, cube_color[side][row][col], [
                    cube_position[side][row][col][0], cube_position[side][row][col][1], piece_size, piece_size])


def draw_piece(pygame, screen, color, location):
    """ Draw piece to the screen with color and location
        Colors: 0 - White, 1 - Green, 2 - Red, 3 - Blue, 4 - Orange, 5 - Yellow
    """
    if color == 0:
        pygame.draw.rect(screen, Color.WHITE_RGB, location)
    elif color == 1:
        pygame.draw.rect(screen, Color.GREEN_RGB, location)
    elif color == 2:
        pygame.draw.rect(screen, Color.RED_RGB, location)
    elif color == 3:
        pygame.draw.rect(screen, Color.BLUE_RGB, location)
    elif color == 4:
        pygame.draw.rect(screen, Color.ORANGE_RGB, location)
    else:
        pygame.draw.rect(screen, Color.YELLOW_RGB, location)
    pygame.draw.rect(screen, Color.BLACK, location, 2)


def draw_text(screen, font, text, location_x, location_y, justify):
    """ Render text on the screen """
    line = font.render(text, True, Color.BLUE_RGB)
    if justify == "LEFT":
        screen.blit(line, (location_x, location_y))
    elif justify == "RIGHT":
        screen.blit(line, (location_x - line.get_width(), location_y))
    elif justify == "CENTER":
        screen.blit(line, (location_x - (line.get_width() / 2.0), location_y))
    else:
        print("Default LEFT")
        screen.blit(line, (location_x, location_y))


def draw_multiple_lines(screen, font, text_list, location_x, location_y, justify, line_spacing):
    """ Render text with multiple lines on the screen """
    space_between_lines = 0
    for sentence in text_list:
        draw_text(screen, font, sentence, location_x,
                  location_y + space_between_lines, justify)
        space_between_lines += line_spacing


def key_pressed(env, event, pygame):
    if event.key == pygame.K_u and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        env.rotate_cube_reverse("U")
        return "U'"
    if event.key == pygame.K_u:
        env.rotate_cube("U")
        return "U"
    if event.key == pygame.K_d and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        env.rotate_cube_reverse("D")
        return "D'"
    if event.key == pygame.K_d:
        env.rotate_cube("D")
        return "D"
    if event.key == pygame.K_l and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        env.rotate_cube_reverse("L")
        return "L'"
    if event.key == pygame.K_l:
        env.rotate_cube("L")
        return "L"
    if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        env.rotate_cube_reverse("R")
        return "R'"
    if event.key == pygame.K_r:
        env.rotate_cube("R")
        return "R"
    if event.key == pygame.K_f and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        env.rotate_cube_reverse("F")
        return "F'"
    if event.key == pygame.K_f:
        env.rotate_cube("F")
        return "F"
    if event.key == pygame.K_b and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        env.rotate_cube_reverse("B")
        return "B'"
    if event.key == pygame.K_b:
        env.rotate_cube("B")
        return "B"
    if event.key == pygame.K_0:
        return env.random_shuffle(number=10)
    return "X"  # Not valid move


def init_cube_position(env, cube_position):
    """ Initialize positions of each piece of the cube """
    num_faces = env.get_num_faces()
    num_pieces_per_face = env.get_num_pieces_per_face()
    num_pieces_per_row = env.get_num_pieces_per_row()
    num_pieces_per_col = env.get_num_pieces_per_col()
    piece_size = env.get_piece_size()
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
                cube_position[side][row][col][1] = row_position + face_row_position
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
