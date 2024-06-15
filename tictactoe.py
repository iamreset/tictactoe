import tkinter as tk

def check_win():
    # Check rows
    for row in matrix:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]

    # Check columns
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != 0:
            return matrix[0][col]

    # Check diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != 0:
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != 0:
        return matrix[0][2]

    return None


def tictactoefn(b, x, y):
    global counter
    if matrix[x][y] == 0:
        if counter % 2 == 0:
            b.config(text="\u2718", fg='blue')           # Heavy Ballot X
            player_label.config(text="Player 2 plays")
            matrix[x][y] = 1
        else:
            b.config(text="\u2713", fg='red')           # Check Mark
            player_label.config(text="Player 1 plays")
            matrix[x][y] = 2
        counter += 1

    winner = check_win()
    if winner:
        disable_all_buttons()
        if winner == 1:
            player_label.config(text="Player 1 has WON!")
        elif winner == 2:
            player_label.config(text="Player 2 has WON!")
    elif counter == 9:
        player_label.config(text="It's a draw!")


def disable_all_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)


def button_text(i):
    if i == 0:
        return "      "
    elif i == 1:
        return "\u25CF"  # Black Circle
    elif i == 2:
        return "\u2713"  # Check Mark


# Global counter
counter = 0

# 3x3 matrix to keep track of the game state
matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

buttons = []

# Create the main application window
root = tk.Tk()
root.title("Tic Tac Toe")

for i in range(3):
    for j in range(3):
        button = tk.Button(root, text=button_text(matrix[i][j]), width=8, height=8, font=("Helvetica", 16))
        button.config(command=lambda b=button, i=i, j=j: tictactoefn(b, i, j))
        button.grid(row=i, column=j)
        buttons.append(button)

# Create a label to display the current player
player_label = tk.Label(root, text="player 1 plays", font=("Helvetica", 16), fg="red", width=30, height=2)
player_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
