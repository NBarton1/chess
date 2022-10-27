owned_pieces = []


def king(square, owned_pieces=owned_pieces):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    left = file >= 2
    right = file <= 7
    down = rank >= 2
    up = rank <= 7

    possible_moves = []

    # Making list of possible moves
    if left and (square-1 not in owned_pieces):
        possible_moves.append(square-1)
    if right and (square+1 not in owned_pieces):
        possible_moves.append(square+1)
    if up and (square+8 not in owned_pieces):
        possible_moves.append(square+8)
    if down and (square-8 not in owned_pieces):
        possible_moves.append(square-8)
    if up and left and (square+7 not in owned_pieces):
        possible_moves.append(square+7)
    if up and right and (square+9 not in owned_pieces):
        possible_moves.append(square+9)
    if left and down and (square-9 not in owned_pieces):
        possible_moves.append(square-9)
    if down and right and (square-7 not in owned_pieces):
        possible_moves.append(square-7)

    return possible_moves


def king_move(square, pieces=owned_pieces):
    # list containing all possible changes in movement
    delta = [-1, 1, -7, 7, -8, 8, -9, 9]
    possible_moves = []

    # loop through all changes
    for d in delta:
        # calculate the new square
        new_square = square + d

        # determine if new_square is legal, absolute difference between new_square % 8 and square % 8 must be 1 or 0
        if -1 < new_square < 64 and abs(square % 8 - new_square % 8) >> 1 == 0 and new_square not in pieces:
            possible_moves.append(new_square)

    return possible_moves


print(king_move(55))
