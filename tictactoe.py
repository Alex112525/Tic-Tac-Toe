symbols = list(input("Enter cells:"))
rows = [symbols[i:i+3] for i in range(0, 9, 3)]
columns = [[symbols[x] for x in range(i, 9, 3)] for i in range(3)]
diagonal_D = [symbols[x] for x in range(0, 9, 4)]
diagonal_I = [symbols[x] for x in range(2, 7, 2)]
O_win = False
X_win = False

space = True if symbols.count("_") >0 else False

print("---------")
for row in rows:
    print("|", end=" ")
    for element in row:
        print(element + " ",end="")
    print("|")
print("---------")

o_number = symbols.count("O")
x_number = symbols.count("X")

X_win = True if diagonal_I.count("X") == 3 else X_win
X_win = True if diagonal_D.count("X") == 3 else X_win

O_win = True if diagonal_I.count("O") == 3 else O_win
O_win = True if diagonal_D.count("O") == 3 else O_win

if not(O_win or X_win):
    for row in rows:
        if row.count("O") == 3:
            O_win = True
        elif row.count("X") == 3:
            X_win = True

    for col in columns:
        if col.count("O") == 3:
            O_win = True
        elif col.count("X") == 3:
            X_win = True

if abs(o_number-x_number) >= 2 or (O_win and X_win):
    print("Impossible")
elif not(O_win or X_win) and space:
    print("Game not finished")
elif not(O_win or X_win) and not space:
    print("Draw")
elif O_win:
    print("O wins")
elif X_win:
    print("X wins")



