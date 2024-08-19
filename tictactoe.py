import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game variables
board = [' ' for _ in range(9)]
current_player = 'X'
buttons = []

def check_winner():
    # Winning conditions
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]  # Diagonal
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != ' ':
            return True
    return False

def click_button(index):
    global current_player

    if board[index] == ' ':
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        messagebox.showwarning("Tic-Tac-Toe", "Invalid move! Try again.")

def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text='')

# Create the Tic-Tac-Toe board using buttons
for i in range(9):
    button = tk.Button(root, text='', font='normal 20 bold', width=5, height=2,
                       command=lambda i=i: click_button(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the main loop to run the application
root.mainloop()

