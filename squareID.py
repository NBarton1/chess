def square_id(coord):
    if coord[0] == "a":
        square = 0
    elif coord[0] == "b":
        square = 1
    elif coord[0] == "c":
        square = 2
    elif coord[0] == "d":
        square = 3
    elif coord[0] == "e":
        square = 4
    elif coord[0] == "f":
        square = 5
    elif coord[0] == "g":
        square = 6
    elif coord[0] == "h":
        square = 7

    square += 8*(int(coord[1]) - 1)
    return square
