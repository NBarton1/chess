pieces = []
white_pieces = []
black_pieces = []


def white_pawn(square, pieces=pieces, black_pieces=black_pieces):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    left = file >= 2
    right = file <= 7

    possible_moves = []

    # Making list of possible moves

    # Move 2 squares on first move
    if rank == 2 and (square+8 not in pieces) and (square+16 not in pieces):
        possible_moves.append(square+16)

    # Move forward
    if rank <= 7 and (square+8 not in pieces):
        possible_moves.append(square+8)

    # Take left
    if left and (square+7 in black_pieces):
        possible_moves.append(square+7)\

    # Take right
    if right and (square+9 in black_pieces):
        possible_moves.append(square+9)

    return possible_moves


def black_pawn(square, pieces=pieces, white_pieces=white_pieces):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    left = file >= 2
    right = file <= 7

    possible_moves = []

    # Making list of possible moves

    # Move 2 squares on first move
    if rank == 7 and (square-8 not in pieces) and (square-16 not in pieces):
        possible_moves.append(square-16)

    # Move forward
    if rank >= 2 and (square-8 not in pieces):
        possible_moves.append(square-8)

    # Take left
    if left and (square-9 in white_pieces):
        possible_moves.append(square-9)

    # Take right
    if right and (square-7 in white_pieces):
        possible_moves.append(square-7)

    return possible_moves
