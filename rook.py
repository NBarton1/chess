pieces = []
owned_pieces = []


def rook(square, pieces=pieces, owned_pieces=owned_pieces):

    # Necessary variables
    rank = (square//8)+1
    file = (square % 8)+1

    start_rank = 8*(rank-1)
    end_rank = 8*rank-1
    start_file = file-1
    end_file = 55+file

    close_left = file-1
    close_right = 8-file
    close_down = rank-1
    close_up = 8-rank

    found_right = False
    found_up = False

    possible_moves = []

    # Rank moves
    for i in pieces:
        for j in range(start_rank, end_rank+1):
            if i == j:
                if j < square:
                    close_left = square-j
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
        for j in range(start_file, end_file+1, 8):
            if i == j:
                if j < square:
                    close_down = (square-j)//8
                    if j in owned_pieces:
                        close_down -= 1
                elif j > square:
                    if not found_up:
                        found_up = True
                        close_up = (j-square)//8
                        if j in owned_pieces:
                            close_up -= 1

    # Making list of possible moves

    # Horizontal
    for i in range(square-close_left, square+close_right+1):
        possible_moves.append(i)

    # Vertical
    for i in range(square-(8*close_down), square+(8*close_up)+1, 8):
        possible_moves.append(i)

    # Removing current square
    while square in possible_moves:
        possible_moves.remove(square)

    return possible_moves
