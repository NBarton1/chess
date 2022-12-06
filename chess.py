import tkinter as tk


# Takes dictionary of pieces and converts to list of squares occupied
def get_squares(pieces):
    pieces_squares = set()
    for i in pieces:
        pieces_squares.add(pieces[i])
    return pieces_squares


# Creates set of possible moves for the queen
def queen(square, owned_pieces_squares, pieces_squares):

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
        if -1 < new_square < 64 and abs(square % 8 - new_square % 8) >> 1 == 0 and new_square not in owned_pieces_squares:
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
        if -1 < new_square < 64 and abs(square % 8 - new_square % 8) - 1 >> 1 == 0 and new_square not in owned_pieces_squares:
            possible_moves.add(new_square)

    return possible_moves


# Creates set of possible moves for the rook
def rook(square, owned_pieces_squares, pieces_squares):

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
def bishop(square, owned_pieces_squares, pieces_squares):

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
    return False


# Determines whether a check is checkmate
def checkmate(owned_pieces, unowned_pieces, pieces, color):
    other_color = "w"
    if color == "w":
        other_color = "b"

    og_owned_pieces = dict(owned_pieces)
    og_unowned_pieces = dict(unowned_pieces)
    og_pieces = dict(pieces)

    for piece in owned_pieces:

        if piece[1] == "p":
            moves = pawn(pieces[piece], get_squares(unowned_pieces), get_squares(pieces), "w")
        elif piece[1] == "n":
            moves = knight(pieces[piece], get_squares(owned_pieces))
        elif piece[1] == "b":
            moves = bishop(pieces[piece], get_squares(owned_pieces), get_squares(pieces))
        elif piece[1] == "r":
            moves = rook(pieces[piece], get_squares(owned_pieces), get_squares(pieces))
        elif piece[1] == "q":
            moves = queen(pieces[piece], get_squares(owned_pieces), get_squares(pieces))
        else:
            moves = king(pieces[piece], get_squares(owned_pieces))

        for move in moves:
            extract = move_piece(pieces[piece], move, owned_pieces, unowned_pieces)
            owned_pieces = extract[0]
            unowned_pieces = extract[1]
            pieces = extract[2]

            if not check(pieces[color+"k"], owned_pieces, unowned_pieces, pieces, other_color):
                return False

            owned_pieces = dict(og_owned_pieces)
            unowned_pieces = dict(og_unowned_pieces)
            pieces = dict(og_pieces)

    return True


# Does a designated move and does necessary captures
def move_piece(square, new_square, owned_pieces, unowned_pieces):
    captured = "none"
    piece = "none"
    for try_piece in owned_pieces:
        if owned_pieces[try_piece] == square:
            piece = try_piece

    if piece != "none":
        owned_pieces[piece] = new_square

        for try_piece in unowned_pieces:
            if unowned_pieces[try_piece] == new_square:
                captured = try_piece

        if captured != "none":
            unowned_pieces.pop(captured)

        return [dict(owned_pieces), dict(unowned_pieces), dict(owned_pieces | unowned_pieces)]


def game(board, square):

    color = "b"
    owned_pieces = dict(board.black_pieces)
    unowned_pieces = dict(board.white_pieces)
    if board.white_turn:
        color = "w"
        owned_pieces = dict(board.white_pieces)
        unowned_pieces = dict(board.black_pieces)

    if not board.select:
        piece = "none"
        for try_piece in owned_pieces:
            if owned_pieces[try_piece] == square:
                piece = try_piece

        if piece != "none":
            board.select = not board.select
            possible_moves = set()
            if piece[1] == "p":
                possible_moves.update(pawn(board.pieces[piece], get_squares(unowned_pieces), get_squares(board.pieces), color))
            elif piece[1] == "n":
                possible_moves.update(knight(board.pieces[piece], get_squares(owned_pieces)))
            elif piece[1] == "b":
                possible_moves.update(bishop(board.pieces[piece], get_squares(owned_pieces), get_squares(board.pieces)))
            elif piece[1] == "r":
                possible_moves.update(rook(board.pieces[piece], get_squares(owned_pieces), get_squares(board.pieces)))
            elif piece[1] == "q":
                possible_moves.update(queen(board.pieces[piece], get_squares(owned_pieces), get_squares(board.pieces)))
            elif piece[1] == "k":
                possible_moves.update(king(board.pieces[piece], get_squares(owned_pieces)))
            board.moves = [square, possible_moves]

    else:
        board.select = not board.select
        if square in board.moves[1]:
            extract = move_piece(board.moves[0], square, dict(owned_pieces), dict(unowned_pieces))
            if not check(extract[0][color + "k"], extract[0], extract[1], extract[2], "w" if color == "b" else "b"):
                board.white_turn = not board.white_turn
                extract = move_piece(board.moves[0], square, owned_pieces, unowned_pieces)

                if color == "w":
                    board.white_pieces = extract[0]
                    board.black_pieces = extract[1]
                else:
                    board.black_pieces = extract[0]
                    board.white_pieces = extract[1]
                board.pieces = extract[2]
                board.update_board()


class boardGUI:

    def __init__(self):

        board = tk.Tk()
        board.title("Chess")
        board.geometry("600x500")
        buttonframe = tk.Frame(board)
        for i in range(8):
            buttonframe.columnconfigure(i, weight=1)

        self.white_pieces = {"wp1": 8, "wp2": 9, "wp3": 10, "wp4": 11, "wp5": 12, "wp6": 13, "wp7": 14, "wp8": 15, "wr1": 0, "wr2": 7, "wn1": 1, "wn2": 6, "wb1": 2, "wb2": 5, "wq1": 3, "wk": 4}
        self.black_pieces = {"bp1": 48, "bp2": 49, "bp3": 50, "bp4": 51, "bp5": 52, "bp6": 53, "bp7": 54, "bp8": 55, "br1": 56, "br2": 63, "bn1": 57, "bn2": 62, "bb1": 58, "bb2": 61, "bq1": 59, "bk": 60}
        self.pieces = self.white_pieces | self.black_pieces

        self.white_turn = True
        self.select = False

        self.moves = [-1, set()]

        self.buttons = []
        for y in range(8):
            for x in range(8):
                color = "#d4d4d4"
                if abs(x-y)%2 == 0:
                    color = "#f2f2f2"
                square = 8*y+x
                btn = tk.Button(buttonframe, text=str(square), font=("Arial", 16), bg=color, command=lambda square=square: game(self, square))
                self.buttons.append(btn)
                btn.grid(row=7 - y, column=x, sticky="we")
        self.update_board()
        buttonframe.pack(pady=50)

        board.mainloop()


    def update_board(self):
        for i, button in enumerate(self.buttons):
            piece = ""
            for try_piece in self.pieces:
                if self.pieces[try_piece] == i:
                    piece = try_piece

            match piece[:2]:
                case "wp":
                    button["text"] = "♙"
                case "wr":
                    button["text"] = "♖"
                case "wn":
                    button["text"] = "♘"
                case "wb":
                    button["text"] = "♗"
                case "wq":
                    button["text"] = "♕"
                case "wk":
                    button["text"] = "♔"

                case "bp":
                    button["text"] = "♟"
                case "br":
                    button["text"] = "♜"
                case "bn":
                    button["text"] = "♞"
                case "bb":
                    button["text"] = "♝"
                case "bq":
                    button["text"] = "♛"
                case "bk":
                    button["text"] = "♚"

                case _:
                    button["text"] = "    "


boardGUI()
