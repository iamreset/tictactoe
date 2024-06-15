import tkinter as tk

# Global counter
counter = 0
''' 3X3 3 states are possible 
            0 at initialization,  
            1 for player 1 and 
            2 for player 2 '''
winning_calc=[[0,0,0],
              [0,0,0],
              [0,0,0]]

# Function to handle button click
def button_clicked(button, i):
    global counter
    if counter % 2 == 0:
        player_label.config(text="player 2 plays")
        button.config(text="\u25CF", state=tk.DISABLED, )  # Black Circle
    else:
        player_label.config(text="player 1 plays")
        button.config(text="\u2713", state=tk.DISABLED)  # Check Mark
    counter += 1

# Create the main application window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create and place buttons in a 3x3 grid
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", width=4, height=4, font=("Helvetica", 30), fg="red")
    button.config(command=lambda b=button, i=i: button_clicked(b, i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Create a label to display the current player
player_label = tk.Label(root, text="player 1 plays", font=("Helvetica", 30), fg="red", width=12, height=2)
player_label.grid(row=3, column=0, columnspan=3)

# Run the main event loop
root.mainloop()

'''
import tkinter as tk
global counter

def buttonf1():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button1.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button1.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


def buttonf2():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button2.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button2.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


def buttonf3():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button3.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button3.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


def buttonf4():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button4.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button4.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


def buttonf5():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button5.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button5.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


def buttonf6():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button6.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button6.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


def buttonf7():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button7.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button7.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


def buttonf8():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button8.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button8.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


def buttonf9():
    if(counter % 2 == 0):
        player_label.config(text="player 2 plays")
        button9.config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 1 plays")
        button9.config(text="\u2713", state=tk.DISABLED)
    counter += 1
    return


counter = 0

root = tk.Tk()
root.title("Tic Tac Toe")

button1 = tk.Button(root, text=" ", width=4, height=4, command=buttonf1)
button2 = tk.Button(root, text=" ", width=4, height=4, command=buttonf2)
button3 = tk.Button(root, text=" ", width=4, height=4, command=buttonf3)
button4 = tk.Button(root, text=" ", width=4, height=4, command=buttonf4)
button5 = tk.Button(root, text=" ", width=4, height=4, command=buttonf5)
button6 = tk.Button(root, text=" ", width=4, height=4, command=buttonf6)
button7 = tk.Button(root, text=" ", width=4, height=4, command=buttonf7)
button8 = tk.Button(root, text=" ", width=4, height=4, command=buttonf8)
button9 = tk.Button(root, text=" ", width=4, height=4, command=buttonf9)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

player_label = tk.Label(root, text="player 1 plays", width=8, height=3)
player_label.grid(row=4, column=1)

root.mainloop()
'''

'''
def button_clicked(i):
    print("counter = ", counter, " i = ", i)
    counter += 1
    if(counter % 2 == 0):
        player_label.config(text="player 1 plays")
        buttons[i].config(text="\u25CF",state=tk.DISABLED)
    else:
        player_label.config(text="player 2 plays")
        buttons[i].config(text="\u2713", state=tk.DISABLED)
    return

global counter
counter = 0

root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize a list for buttons with None values
buttons = [None] * 10

# Create buttons and store them in the list
for i in range(1, 10):
    buttons[i] = tk.Button(root, text="  ", width=4, height=4, command=lambda i=i: button_clicked(i))
    # Place the buttons in a 3x3 grid
    buttons[i].grid(row=(i-1)//3, column=(i-1)%3)

player_label = tk.Label(root, text="player 1 plays", width=8, height=3)
player_label.grid(row=4, column=1)

# Run the main event loop
root.mainloop()
'''

'''def calculate(button_id):
    result = button_id * 10
    print(f"Button ID: {button_id}, Result: {result}")
    changePlayer()
    disableButton(button_id)

def disableButton(button_id):
    

def changePlayer():
    button_player_counter += 1
    if button_player_counter % 2 == 1:
        button_player.config(text="player 2 plays")
    else:
        button_player.config(text="player 1 plays")


# Create the main application window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create a dictionary to store button IDs
button_ids = {
    "Button 1": [1, 0],
    "Button 2": [2, 0],
    "Button 3": [3, 0],
    "Button 4": [4, 0],
    "Button 5": [5, 0],
    "Button 6": [6, 0],
    "Button 7": [7, 0],
    "Button 8": [8, 0],
    "Button 9": [9, 0]
}

global button_player_counter = 1

# Create and place buttons
for button_name, button_id in button_ids.items():
    # Bind each button to a lambda function that calls calculate with the button_id
    x = int((button_id[0] - 1) / 3)
    y = (button_id[0] - 1) % 3
    print(x,y)
    button = tk.Button(root, text="  ", width=4, height=4, command=lambda id=button_id[0]: calculate(id))
    button.grid(row=x, column=y)

button_player = tk.Label(root, text="player 1 plays", width=8, height=3)
button_player.grid(row=4, column=1)



# Run the main event loop
root.mainloop()
'''
'''
def tactoe():
    return


root = Tk()
root.config(background='blue', width=200, highlightbackground='blue', height=200, relief="raised")

button_text = "   "
button = list(range(9))
counter = 0
for x in range(3):
    for y in range(3):
        i = (3*x)+y
        button[i] = Button(root, text=i, width=4, height=4, bg='blue', fg='blue', command=tactoe)
        button[i].grid(row=x, column=y)

root.mainloop()
'''