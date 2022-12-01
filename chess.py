# Lists of pieces
white_pieces = {"wk": 7}
black_pieces = {"bp": 15}
pieces = white_pieces | black_pieces


# Takes dictionary of pieces and converts to list of squares occupied
def get_squares(pieces):
    pieces_squares = set()
    for i in pieces:
        pieces_squares.add(pieces[i])
    return pieces_squares


# Creates set of possible moves for the queen
def queen(square, owned_pieces_squares, pieces_squares=get_squares(pieces)):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    close_left = file - 1
    close_right = 8 - file
    close_down = rank - 1
    close_up = 8 - rank

    close_down_left = min(rank, file) - 1
    close_up_right = min(9 - rank, 9 - file) - 1
    close_down_right = min(rank, 9 - file) - 1
    close_up_left = min(9 - rank, file) - 1

    start_rank = 8 * (rank - 1)
    end_rank = 8 * rank - 1
    start_file = file - 1
    end_file = 55 + file

    start_pos_diagonal = square - (9 * close_down_left)
    end_pos_diagonal = square + (9 * close_up_right)
    start_neg_diagonal = square - (7 * close_down_right)
    end_neg_diagonal = square + (7 * close_up_left)

    possible_moves = set()

    # Rank moves
    for i in range(start_rank, end_rank + 1):
        if i in pieces_squares and i < square:
            close_left = square - i
            if i in owned_pieces_squares:
                close_left -= 1
        elif i in pieces_squares and i > square:
            close_right = i - square
            if i in owned_pieces_squares:
                close_right -= 1
            break

    # File moves
    for i in range(start_file, end_file + 1, 8):
        if i in pieces_squares and i < square:
            close_down = (square - i) // 8
            if i in owned_pieces_squares:
                close_down -= 1
        elif i in pieces_squares and i > square:
            close_up = (i - square) // 8
            if i in owned_pieces_squares:
                close_up -= 1
            break

    # Positive diagonal moves
    for i in range(start_pos_diagonal, end_pos_diagonal + 1, 9):
        if i in pieces_squares and i < square:
            close_down_left = (square - i) // 9
            if i in owned_pieces_squares:
                close_down_left -= 1
        elif i in pieces_squares and i > square:
            close_up_right = (i - square) // 9
            if i in owned_pieces_squares:
                close_up_right -= 1
            break

    # Negative diagonal moves
    for i in range(start_neg_diagonal, end_neg_diagonal + 1, 7):
        if i in pieces_squares and i < square:
            close_down_right = (square - i) // 7
            if i in owned_pieces_squares:
                close_down_right -= 1
        elif i in pieces_squares and i > square:
            close_up_left = (i - square) // 7
            if i in owned_pieces_squares:
                close_up_left -= 1
            break

    # Making list of possible moves

    # Horizontal
    for i in range(square - close_left, square + close_right + 1):
        possible_moves.add(i)

    # Vertical
    for i in range(square - (8 * close_down), square + (8 * close_up) + 1, 8):
        possible_moves.add(i)

    # Positive diagonal
    for i in range(square - (9 * close_down_left), square + (9 * close_up_right) + 1, 9):
        possible_moves.add(i)

    # Negative diagonal
    for i in range(square - (7 * close_down_right), square + (7 * close_up_left) + 1, 7):
        possible_moves.add(i)

    # Removing current square
    possible_moves.remove(square)

    return possible_moves


# Creates set of possible moves for the king
def king(square, owned_pieces_squares):

    # List containing all possible changes in movement
    delta = [-1, 1, -7, 7, -8, 8, -9, 9]
    possible_moves = set()

    # Loop through all changes
    for d in delta:

        # Calculate the new square
        new_square = square + d

        # Determine if new_square is legal, absolute difference between new_square % 8 and square % 8 must be 1 or 0
        if -1 < new_square < 64 and abs(
                square % 8 - new_square % 8) >> 1 == 0 and new_square not in owned_pieces_squares:
            possible_moves.add(new_square)

    return possible_moves


# Creates set of possible moves for the knight
def knight(square, owned_pieces_squares):

    # List containing all possible changes in movement
    delta = [-6, 6, -10, 10, -15, 15, -17, 17]
    possible_moves = set()

    # Loop through all changes
    for d in delta:

        # Calculate the new square
        new_square = square + d

        # Determine if new_square is legal, absolute difference between new_square % 8 and square % 8 must be 2 or 1
        if -1 < new_square < 64 and abs(
                square % 8 - new_square % 8) - 1 >> 1 == 0 and new_square not in owned_pieces_squares:
            possible_moves.add(new_square)

    return possible_moves


# Creates set of possible moves for the rook
def rook(square, owned_pieces_squares, pieces_squares=get_squares(pieces)):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    start_rank = 8 * (rank - 1)
    end_rank = 8 * rank - 1
    start_file = file - 1
    end_file = 55 + file

    close_left = file - 1
    close_right = 8 - file
    close_down = rank - 1
    close_up = 8 - rank

    possible_moves = set()

    # Rank moves
    for i in range(start_rank, end_rank + 1):
        if i in pieces_squares and i < square:
            close_left = square - i
            if i in owned_pieces_squares:
                close_left -= 1
        elif i in pieces_squares and i > square:
            close_right = i - square
            if i in owned_pieces_squares:
                close_right -= 1
            break

    # File moves
    for i in range(start_file, end_file + 1, 8):
        if i in pieces_squares and i < square:
            close_down = (square - i) // 8
            if i in owned_pieces_squares:
                close_down -= 1
        elif i in pieces_squares and i > square:
            close_up = (i - square) // 8
            if i in owned_pieces_squares:
                close_up -= 1
            break

    # Making list of possible moves

    # Horizontal
    for i in range(square - close_left, square + close_right + 1):
        possible_moves.add(i)

    # Vertical
    for i in range(square - (8 * close_down), square + (8 * close_up) + 1, 8):
        possible_moves.add(i)

    # Removing current square
    possible_moves.remove(square)

    return possible_moves


# Creates set of possible moves for the bishop
def bishop(square, owned_pieces_squares, pieces_squares=get_squares(pieces)):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    close_down_left = min(rank, file) - 1
    close_up_right = min(9 - rank, 9 - file) - 1
    close_down_right = min(rank, 9 - file) - 1
    close_up_left = min(9 - rank, file) - 1

    start_pos_diagonal = square - (9 * close_down_left)
    end_pos_diagonal = square + (9 * close_up_right)
    start_neg_diagonal = square - (7 * close_down_right)
    end_neg_diagonal = square + (7 * close_up_left)

    possible_moves = set()

    # Positive diagonal moves
    for i in range(start_pos_diagonal, end_pos_diagonal + 1, 9):
        if i in pieces_squares and i < square:
            close_down_left = (square - i) // 9
            if i in owned_pieces_squares:
                close_down_left -= 1
        elif i in pieces_squares and i > square:
            close_up_right = (i - square) // 9
            if i in owned_pieces_squares:
                close_up_right -= 1
            break

    # Negative diagonal moves
    for i in range(start_neg_diagonal, end_neg_diagonal + 1, 7):
        if i in pieces_squares and i < square:
            close_down_right = (square - i) // 7
            if i in owned_pieces_squares:
                close_down_right -= 1
        elif i in pieces_squares and i > square:
            close_up_left = (i - square) // 7
            if i in owned_pieces_squares:
                close_up_left -= 1
            break

    # Making list of possible moves

    # Positive diagonal
    for i in range(square - (9 * close_down_left), square + (9 * close_up_right) + 1, 9):
        possible_moves.add(i)

    # Negative diagonal
    for i in range(square - (7 * close_down_right), square + (7 * close_up_left) + 1, 7):
        possible_moves.add(i)

    # Removing current square
    possible_moves.remove(square)

    return possible_moves


# Creates set of possible moves for the white pawns
def pawn(square, unowned_pieces_squares, pieces_squares, color):

    # Necessary variables
    rank = (square // 8) + 1
    file = (square % 8) + 1

    left = file >= 2
    right = file <= 7

    possible_moves = set()

    indicator = -8
    if color == "w":
        indicator = 8

    # Making list of possible moves

    # Move 2 squares on first move
    if ((rank == 2 and color == "w") or (rank == 7 and color == "b")) and (square + indicator not in pieces_squares) and (square + 2 * indicator not in pieces_squares):
        possible_moves.add(square + 2 * indicator)

    # Move forward
    if ((color == "w" and rank <= 7) or (color == "b" and rank >= 2)) and (square + indicator not in pieces_squares):
        possible_moves.add(square + indicator)

    # Take left
    if left and (square + indicator - 1 in unowned_pieces_squares):
        possible_moves.add(square + indicator - 1)

        # Take right
    if right and (square + indicator + 1 in unowned_pieces_squares):
        possible_moves.add(square + indicator + 1)

    return possible_moves


# Determines whether the king is in check
def check(square, owned_pieces, unowned_pieces, pieces, other_color):
    opponent_moves = set()
    for piece in unowned_pieces:
        if piece[1] == "p":
            opponent_moves.update(pawn(pieces[piece], get_squares(owned_pieces), get_squares(pieces), other_color))
        elif piece[1] == "n":
            opponent_moves.update(knight(pieces[piece], get_squares(unowned_pieces)))
        elif piece[1] == "b":
            opponent_moves.update(bishop(pieces[piece], get_squares(unowned_pieces), get_squares(pieces)))
        elif piece[1] == "r":
            opponent_moves.update(rook(pieces[piece], get_squares(unowned_pieces), get_squares(pieces)))
        elif piece[1] == "q":
            opponent_moves.update(queen(pieces[piece], get_squares(unowned_pieces), get_squares(pieces)))
        elif piece[1] == "k":
            opponent_moves.update(king(pieces[piece], get_squares(unowned_pieces)))

    if square in opponent_moves:
        return True
    else:
        return False


# 56 57 58 59 60 61 62 63
# 48 49 50 51 52 53 54 55
# 40 41 42 43 44 45 46 47
# 32 33 34 35 36 37 38 39
# 24 25 26 27 28 29 30 31
# 16 17 18 19 20 21 22 23
# 08 09 10 11 12 13 14 15
# 00 01 02 03 04 05 06 07
