import pygame.image

import pieces
import updating_grid

global score, piece_is_moving_right, piece_is_moving_left, current_piece, passive_grid, progress, level, game_over

red_cube = pygame.image.load("red_cube.png")
blue_cube = pygame.image.load("blue_cube.png")
green_cube = pygame.image.load("green_cube.png")
cubes = [red_cube, blue_cube, green_cube]

# passive grid is 14 blocks tall
passive_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def test_death():
    global game_over
    for x in range(len(passive_grid[0])):
        if (passive_grid[0][x] >= 1): game_over = True


def prepare_game():
    global game_over, score, progress, level
    game_over = False
    level = 1
    progress = 0
    score = 0
    updating_grid.target_falling_speed = 0.05
    updating_grid.falling_speed = 0.05


def reset_game():
    global game_over
    for y in range(len(passive_grid)):
        for x in range(len(passive_grid[y])):
            passive_grid[y][x] = 0
    updating_grid.clear_active_grid()
    prepare_game()


def test_horizontal_block_collision():
    for y in range(len(passive_grid)):
        for x in range(len(passive_grid[y])):
            try:
                if updating_grid.active_grid[y + 4][x] >= 1 and passive_grid[y][x + 1] >= 1:
                    pieces.can_move_right = True
                if updating_grid.active_grid[y + 4][x] >= 1 and passive_grid[y][x - 1] >= 1:
                    pieces.can_move_left = True
            except IndexError:
                return 0


def test_bottom_of_grid_collision():
    if (int(updating_grid.piece_pos_y) == 18 - len(
            pieces.current_piece)):  # check if the piece has hit the bottom of the screen
        place_piece()


def test_verticle_block_collision():
    exit_y_loop = False
    for y in range(len(passive_grid)):
        if exit_y_loop:
            break  # ensures that the place piece function only gets called once

        for x in range(len(passive_grid[y])):  # check if a piece is above a placed piece
            if passive_grid[y][x] >= 1 and updating_grid.active_grid[y + 3][x] >= 1:
                place_piece()
                exit_y_loop = True
                break  # ensures that the place piece function only gets called once


def test_piece_collision():  # this function is called to test the collision of the pieces
    test_horizontal_block_collision()
    test_verticle_block_collision()
    test_bottom_of_grid_collision()


def place_piece():
    for y in range(len(updating_grid.active_grid)):
        for x in range(len(updating_grid.active_grid[y])):
            if (passive_grid[y - 4][x] == 0):
                passive_grid[y - 4][x] = updating_grid.active_grid[y][
                    x]  # copies the entire active grid to the passive grid

    updating_grid.reset_piece()
    pieces.set_piece_target(pieces.next_piece)


def shift_rows(row):
    current_row = row
    while current_row != 0:
        for x in range(len(passive_grid[current_row])):
            passive_grid[current_row][x] = passive_grid[current_row - 1][x]
        current_row -= 1


def detect_full_line():
    for y in range(
            len(passive_grid)):  # loop through the passive grid and check if each line is full then clear and shift it if it is
        count = 0
        for x in range(len(passive_grid[y])):
            if passive_grid[y][x] != 0:
                count += 1
                if (count >= 10):
                    shift_rows(y)
                    check_progress()


def check_progress():
    global progress, level, score

    progress += 1
    score += 100
    if (progress >= 10):
        progress = 0
        level += 1
        updating_grid.increase_difficulty()


def check_changes():
    global current_piece

    test_death()
    updating_grid.update_piece(pieces.get_current_piece())
    test_piece_collision()
    updating_grid.update_movement()
    detect_full_line()
