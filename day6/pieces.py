import random

global current_piece, target_piece, piece_rotation, can_move_left, can_move_right, next_piece
Long_piece = \
    [[0], [0, 3, 3, 3, 3, 0]], \
    [
        [0, 3],
        [0, 3],
        [0, 3, 0],
        [0, 3]]
T_piece = \
    [[0, 0, 2, 0],
     [0, 2, 2, 2, 0]], \
    [[0, 2, 0],
     [0, 2, 2, 0],
     [0, 2, 0]], \
    [[0, 0, 0],
     [0, 2, 2, 2, 0],
     [0, 0, 2, 0]], \
    [[0, 0, 2, 0],
     [0, 2, 2, 0],
     [0, 0, 2, 0]]

Cube_piece = \
    [[0],
     [0, 3, 3, 0],
     [0, 3, 3, 0]], [[0],
                     [0, 3, 3, 0],
                     [0, 3, 3, 0]]
L_piece = \
    [[0, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0], ], \
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0], ], \
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 1, 0], ], \
    [[0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 1, 0, 0, 0], ]
RL_piece = \
    [[0, 2, 2, 0],
     [0, 2, 0, 0],
     [0, 2, 0, 0], ], \
    [[0, 0, 0, 0, 0],
     [0, 2, 2, 2, 0],
     [0, 0, 0, 2, 0], ], \
    [[0, 0, 2, 0],
     [0, 0, 2, 0],
     [0, 2, 2, 0], ], \
    [[0, 0, 0, 0, 0],
     [0, 2, 0, 0, 0],
     [0, 2, 2, 2, 0]]
S_piece = \
    [[0, 0, 3, 3, 0],
     [0, 3, 3, 0, 0], ], \
    [[0, 3, 0, 0],
     [0, 3, 3, 0],
     [0, 0, 3, 0], ]

Z_piece = \
    [[0, 0, 1, 0],
     [0, 1, 1, 0],
     [0, 1, 0, 0], ], \
    [[0, 1, 1, 0, 0],
     [0, 0, 1, 1, 0], ]

can_move_right = False
can_move_left = False
target_piece = "Long_piece"
next_piece = "Cube_piece"
piece_list_names = ["Long_piece", "T_piece", "Cube_piece", "L_piece", "RL_piece", "S_piece", "Z_piece"]
piece_list_object = [Long_piece, T_piece, Cube_piece, L_piece, RL_piece, S_piece, Z_piece]
piece_rotation = 0  # determines rotation of piece
max_rotation = 1  # determines how many times a piece can rotate
current_piece = Long_piece[0]


def randomized_piece():
    global next_piece
    random_value = random.randrange(0, 7, 1)
    next_piece = piece_list_names[random_value]
    if (random_value == 6 or random_value == 5):
        if (random.randrange(0, 2, 1) == 0): next_piece = piece_list_names[random.randrange(0, 7, 1)]


def rotate(direction):
    global piece_rotation, max_rotation
    if (direction == "right"):
        piece_rotation += 1
    if (direction == "left"):
        piece_rotation -= 1
    if (piece_rotation < 0):
        piece_rotation = max_rotation
    if (piece_rotation > max_rotation):
        piece_rotation = 0


def set_piece_target(wanted_piece):
    global piece_rotation, target_piece
    piece_rotation = 0
    target_piece = wanted_piece
    randomized_piece()


def update_piece():
    global current_piece, max_rotation

    for piece_number in range(len(piece_list_names)):
        if (target_piece == piece_list_names[piece_number]):
            max_rotation = len(piece_list_object[piece_number]) - 1
            current_piece = piece_list_object[piece_number][piece_rotation]
            break


def get_current_piece():
    global current_piece
    return current_piece
