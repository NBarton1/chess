owned_pieces = []


def king(square, owned_pieces=owned_pieces):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    move_left = file >= 2
    move_right = file <= 7
    move_down = rank >= 2
    move_up = rank <= 7

    possible_moves = []

    # Making list of possible moves
    if move_left and (square-1 not in owned_pieces):
        possible_moves.append(square-1)
    if move_right and (square+1 not in owned_pieces):
        possible_moves.append(square+1)
    if move_up and (square+8 not in owned_pieces):
        possible_moves.append(square+8)
    if move_down and (square-8 not in owned_pieces):
        possible_moves.append(square-8)
    if move_up and move_left and (square+7 not in owned_pieces):
        possible_moves.append(square+7)
    if move_up and move_right and (square+9 not in owned_pieces):
        possible_moves.append(square+9)
    if move_left and move_down and (square-9 not in owned_pieces):
        possible_moves.append(square-9)
    if move_down and move_right and (square-7 not in owned_pieces):
        possible_moves.append(square-7)

    return possible_moves


while True:
    print(king(int(input())))
