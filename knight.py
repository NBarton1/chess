owned_pieces = []


def knight(square, owned_pieces=owned_pieces):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    left = file >= 2
    left2 = file >= 3
    right = file <= 7
    right2 = file <= 6
    up = rank <= 7
    up2 = rank <= 6
    down = rank >= 2
    down2 = rank >= 3

    possible_moves = []

    # Making list of possible moves
    if left and up2 and (square+15 not in owned_pieces):
        possible_moves.append(square+15)
    if left2 and up and (square+6 not in owned_pieces):
        possible_moves.append(square+6)
    if left and down2 and (square-17 not in owned_pieces):
        possible_moves.append(square-17)
    if left2 and down and (square-10 not in owned_pieces):
        possible_moves.append(square-10)
    if right and up2 and (square+17 not in owned_pieces):
        possible_moves.append(square+17)
    if right2 and up and (square+10 not in owned_pieces):
        possible_moves.append(square+10)
    if right and down2 and (square-15 not in owned_pieces):
        possible_moves.append(square-15)
    if right2 and down and (square-6 not in owned_pieces):
        possible_moves.append(square-6)

    return possible_moves


def knight_move(square, pieces=owned_pieces):
    # list containing all possible changes in movement
    delta = [-6, 6, -10, 10, -15, 15, -17, 17]
    possible_moves = []

    # loop through all changes
    for d in delta:
        # calculate the new square
        new_square = square + d

        # determine if new_square is legal, absolute difference between new_square % 8 and square % 8 must be 2 or 1
        if -1 < new_square < 64 and abs(square % 8 - new_square % 8) - 1 >> 1 == 0 and new_square not in pieces:
            possible_moves.append(new_square)

    return possible_moves


print(knight_move(32))
