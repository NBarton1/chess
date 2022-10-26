pieces = []
owned_pieces = []


def queen(square, pieces=pieces, owned_pieces=owned_pieces):

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

    close_down_left = min(rank, file) - 1
    close_up_right = min(9 - rank, 9 - file) - 1
    close_down_right = min(rank, 9 - file) - 1
    close_up_left = min(9 - rank, file) - 1

    start_pos_diagonal = square - (9 * close_down_left)
    end_pos_diagonal = square + (9 * close_up_right)
    start_neg_diagonal = square - (7 * close_down_right)
    end_neg_diagonal = square + (7 * close_up_left)

    found_right = False
    found_up = False
    found_up_right = False
    found_up_left = False

    possible_moves = []

    # Rank moves
    for i in pieces:
        for j in range(start_rank, end_rank + 1):
            if i == j:
                if j < square:
                    close_left = square - j
                    if j in owned_pieces:
                        close_left -= 1
                elif j > square:
                    if not found_right:
                        found_right = True
                        close_right = j - square
                        if j in owned_pieces:
                            close_right -= 1

    # File moves
    for i in pieces:
        for j in range(start_file, end_file + 1, 8):
            if i == j:
                if j < square:
                    close_down = (square - j) // 8
                    if j in owned_pieces:
                        close_down -= 1
                elif j > square:
                    if not found_up:
                        found_up = True
                        close_up = (j - square) // 8
                        if j in owned_pieces:
                            close_up -= 1

    # Positive diagonal moves
    for i in pieces:
        for j in range(start_pos_diagonal, end_pos_diagonal + 1, 9):
            if i == j:
                if j < square:
                    close_down_left = (square - j) // 9
                    if j in owned_pieces:
                        close_down_left -= 1
                elif j > square:
                    if not found_up_right:
                        found_up_right = True
                        close_up_right = (j - square) // 9
                        if j in owned_pieces:
                            close_up_right -= 1

    # Negative diagonal moves
    for i in pieces:
        for j in range(start_neg_diagonal, end_neg_diagonal + 1, 7):
            if i == j:
                if j < square:
                    close_down_right = (square - j) // 7
                    if j in owned_pieces:
                        close_down_right -= 1
                elif j > square:
                    if not found_up_left:
                        found_up_left = True
                        close_up_left = (j - square) // 7
                        if j in owned_pieces:
                            close_up_left -= 1

    # Making list of possible moves

    # Horizontal
    for i in range(square-close_left, square+close_right+1):
        possible_moves.append(i)

    # Vertical
    for i in range(square-(8*close_down), square+(8*close_up)+1, 8):
        possible_moves.append(i)

    # Positive diagonal
    for i in range(square - (9 * close_down_left), square + (9 * close_up_right) + 1, 9):
        possible_moves.append(i)

    # Negative diagonal
    for i in range(square - (7 * close_down_right), square + (7 * close_up_left) + 1, 7):
        possible_moves.append(i)

    # Removing current square
    while square in possible_moves:
        possible_moves.remove(square)

    return possible_moves
