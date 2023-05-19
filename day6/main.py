import pygame
import grid, updating_grid

import pieces


def setup_window():
    global background_color, Window, window_height, window_width, running, play_area, update_rate, piece_display, game_over_display

    pygame.font.init()
    pygame.display.set_caption("Tetris Project - By Dustin Terry")
    window_height = 900
    window_width = 800
    background_color = (0, 0, 0)
    Window = pygame.display.set_mode((window_width, window_height))  # creates window for the game to run in
    running = True
    piece_display = pygame.image.load("L_piece.png")
    game_over_display = pygame.image.load("game_over.png")
    play_area = pygame.image.load("play_area.png")
    update_rate = pygame.time.Clock()


def display_text(text, x, y, size, color):  # function is used for displaying text
    font = pygame.font.Font("freesansbold.ttf", size)
    # font = pygame.font.SysFont('comicsansms', size)
    # print(pygame.font.get_fonts())
    white = (255, 255, 255)
    red = 255, 0, 0
    if color == "white":
        text = font.render(text, True, white)
    if color == "red":
        text = font.render(text, True, red)
    Window.blit(text, (x, y))


def monitor_keys(event):
    if event.type == pygame.KEYDOWN:
       match event.key:  # activates when key has been pressed
            case pygame.K_DOWN:
                updating_grid.increase_drop_speed()
            case pygame.K_RIGHT:
                updating_grid.piece_is_moving_right = True
            case pygame.K_LEFT:
                updating_grid.piece_is_moving_left = True
            case pygame.K_v:
                pieces.rotate("right")
            case pygame.K_c:
                pieces.rotate("left")
            case pygame.K_RETURN:
               if grid.game_over:
                   grid.reset_game()

    if event.type == pygame.KEYUP:
       match event.key:  # activates when key has been released
            case pygame.K_DOWN:
                updating_grid.reset_drop_speed()
            case pygame.K_RIGHT:
                updating_grid.piece_is_moving_right = False
            case pygame.K_LEFT:
                updating_grid.piece_is_moving_left = False


def draw_pieces(target_grid, y_offset):
    for y in range(len(target_grid)):
        for x in range(len(target_grid[y])):
            value = target_grid[y][x]
            if value != 0:
                Window.blit(grid.cubes[value - 1], ((x * 60) + 20, (y * 60) - (17 + y_offset)))


def update_game():
    global running, update_rate
    for event in pygame.event.get():
        monitor_keys(event)
        if event.type == pygame.QUIT:
            running = False  # terminates the game
    if not (grid.game_over):
        grid.check_changes()
    update_rate.tick(40)


def update_graphics():
    global piece_display, game_over_display
    piece_name = pieces.next_piece
    piece_display = pygame.image.load(piece_name + ".png")

    Window.fill(background_color)  # gives the game something to draw on
    display_text("current score", window_width - 175, 10, 20, "white")
    display_text(str(grid.score), window_width - 175, 30, 20, "white")
    display_text("current level", window_width - 175, 50, 20, "white")
    display_text(str(grid.level), window_width - 175, 70, 20, "white")
    display_text("next piece", window_width - 175, 90, 20, "white")
    display_text("Controls:", window_width - 175, 390, 20, "white")
    display_text("Rotate: C or V", window_width - 175, 420, 20, "white")
    display_text("Move:Arrow Keys", window_width - 175, 450, 20, "white")

    Window.blit(play_area, (20, 20))  # displays background for the stackable squares

    draw_pieces(grid.passive_grid, 0)
    draw_pieces(updating_grid.active_grid, 240)

    Window.blit(piece_display, (window_width - 180, 120))
    if (grid.game_over): Window.blit(game_over_display, (20, 20))
    pygame.display.update()


def main():
    setup_window()
    grid.prepare_game()
    while running:
        update_game()
        update_graphics()


main()
