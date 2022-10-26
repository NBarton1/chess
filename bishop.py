pieces = []
owned_pieces = []


def bishop(square, pieces=pieces, owned_pieces=owned_pieces):

    # Necessary variables
    rank = (square//8)+1
    file = (square % 8)+1

    close_down_left = min(rank, file)-1
    close_up_right = min(9-rank, 9-file)-1
    close_down_right = min(rank, 9-file)-1
    close_up_left = min(9-rank, file)-1

    start_pos_diagonal = square-(9*close_down_left)
    end_pos_diagonal = square+(9*close_up_right)
    start_neg_diagonal = square-(7*close_down_right)
    end_neg_diagonal = square+(7*close_up_left)

    found_up_right = False
    found_up_left = False

    possible_moves = []

    # Positive diagonal moves
    for i in pieces:
        for j in range(start_pos_diagonal, end_pos_diagonal+1, 9):
            if i == j:
                if j < square:
                    close_down_left = (square-j)//9
                    if j in owned_pieces:
                        close_down_left -= 1
                elif j > square:
                    if not found_up_right:
                        found_up_right = True
                        close_up_right = (j-square)//9
                        if j in owned_pieces:
                            close_up_right -= 1

    # Negative diagonal moves
    for i in pieces:
        for j in range(start_neg_diagonal, end_neg_diagonal+1, 7):
            if i == j:
                if j < square:
                    close_down_right = (square-j)//7
                    if j in owned_pieces:
                        close_down_right -= 1
                elif j > square:
                    if not found_up_left:
                        found_up_left = True
                        close_up_left = (j-square)//7
                        if j in owned_pieces:
                            close_up_left -= 1

    # Making list of possible moves

    # Positive diagonal
    for i in range(square-(9*close_down_left), square+(9*close_up_right)+1, 9):
        possible_moves.append(i)

    # Negative diagonal
    for i in range(square-(7*close_down_right), square+(7*close_up_left)+1, 7):
        possible_moves.append(i)

    # Removing current square
    while square in possible_moves:
        possible_moves.remove(square)

    return possible_moves


while True:
    print(bishop(int(input())))
