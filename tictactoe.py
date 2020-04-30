def winner(state, rows_):
    columns = [[state[x] for x in range(i, 9, 3)] for i in range(3)]
    diagonal_D = [state[x] for x in range(0, 9, 4)]
    diagonal_I = [state[x] for x in range(2, 7, 2)]

    space = True if state.count(" ") > 0 else False

    o_win = False
    x_win = False

    # o_number = symbols.count("O")
    # x_number = symbols.count("X")

    x_win = True if diagonal_I.count("X") == 3 else x_win
    x_win = True if diagonal_D.count("X") == 3 else x_win

    o_win = True if diagonal_I.count("O") == 3 else o_win
    o_win = True if diagonal_D.count("O") == 3 else o_win

    if not (o_win or x_win):
        for row in rows_:
            if row.count("O") == 3:
                o_win = True
            elif row.count("X") == 3:
                x_win = True

        for col in columns:
            if col.count("O") == 3:
                o_win = True
            elif col.count("X") == 3:
                x_win = True

    # if abs(o_number - x_number) >= 2 or (o_win and x_win):
    # print("Impossible")
    # return True
    # elif not (o_win or x_win) and space:
    # print("Game not finished")
    if not (o_win or x_win) and not space:
        print("Draw")
        return True
    elif o_win:
        print("O wins")
        return True
    elif x_win:
        print("X wins")
        return True
    else:
        return False


def print_game(matrix):
    print("---------")
    for row in matrix:
        print("|", end=" ")
        for element in row:
            print(element + " ", end="")
        print("|")
    print("---------")


symbols = list("         ")
rows = [symbols[i:i + 3] for i in range(0, 9, 3)]

print_game(rows)

rep = True
input_ = True
Game = False
player = True

while not Game:
    while input_:
        try:
            x, y = map(int, input("Enter the coordinates: ").split())
        except:
            print("You should enter numbers!")
        else:
            if x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
            else:
                input_ = False
    x -= 1
    if y == 3:
        y = 0
    elif y == 2:
        y = 1
    elif y == 1:
        y = 2

    if rows[y][x] == "X" or rows[y][x] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        if player:
            rows[y][x] = "X"
        else:
            rows[y][x] = "O"
        print_game(rows)
        player = not player
    input_ = True

    x = []
    for n in rows:
        x.append("".join(n))
    y = "".join(x)

    Game = winner(y, rows)
