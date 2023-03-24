import pieces

global piece_pos_x, piece_pos_y, falling_speed
piece_is_moving_left = False  # determines if a piece is moving left
piece_is_moving_right = False  # determines if a piece is moving right

left_right_speed = 0.3  # determines left right movement speed of falling piece
piece_pos_y = 0.0  # determines y value of falling piece
piece_pos_x = 4.0  # determines x value of falling piece
falling_speed = 0.05  # determines speed of falling piece

drop_speed = 0.35
target_falling_speed = 0.05

# active grid will be 4 blocks taller than the passive grid
# active grid is 18 blocks tall
active_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def reset_piece():
    global piece_pos_x, piece_pos_y
    pieces.can_move_right = False
    pieces.can_move_left = False
    piece_pos_y = 0
    piece_pos_x = 4


def increase_drop_speed():
    global falling_speed
    falling_speed = drop_speed + target_falling_speed


def reset_drop_speed():
    global falling_speed
    falling_speed = target_falling_speed


def clear_active_grid():
    for y in range(len(active_grid)):
        for x in range(len(active_grid[y])):
            active_grid[y][x] = 0


def update_piece(piece):
    clear_active_grid()
    for piece_height in range(len(piece)):  # cycle through the selected piece
        for piece_width in range(len(piece[piece_height])):  # cycle through the width of the piece

            if int(piece_pos_x) + piece_width < 10 and not int(
                    piece_pos_x) + piece_width < 0:  # only add the block to the grid if its fully on the grid

                active_grid[int(piece_pos_y) + piece_height][int(piece_pos_x) + piece_width] = piece[piece_height][
                    piece_width]  # add piece to the active grid

            test_sidewall_collision(piece_width)


def test_sidewall_collision(x):
    global piece_is_moving_left, piece_is_moving_right, piece_pos_x

    if int(piece_pos_x) + x > 9:  # implement collision on the right side
        piece_is_moving_right = False
        if int(piece_pos_x) + x == 11:  # stop players from glitching the pieces into the walls
            piece_pos_x -= 1
    if int(piece_pos_x) < -1:  # implement collision on the left side
        piece_is_moving_left = False
        if int(piece_pos_x) + x == -2:  # stop players from glitching the pieces into the walls
            piece_pos_x += 1


def increase_difficulty():
    global target_falling_speed
    target_falling_speed = target_falling_speed + 0.03


def update_movement():
    global piece_pos_x, piece_pos_y

    piece_pos_y += falling_speed  # updates downward piece movement
    pieces.update_piece()

    # updates left and right movement based off keyboard actions
    if (piece_is_moving_left):
        if not pieces.can_move_left:
            piece_pos_x -= left_right_speed  # move the piece left if there is no block on the right
        pieces.can_move_right = False  # acknoledge that a piece could move right when it moves left
    if (piece_is_moving_right):
        if not pieces.can_move_right:
            piece_pos_x += left_right_speed  # move the piece right if there is no block on the right
        pieces.can_move_left = False  # acknoledge that a piece could move left when it moves right
