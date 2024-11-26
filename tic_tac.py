import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for index in combo:
                buttons[index].config(bg="yellow")  # Highlight winning buttons
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        if current_player == "X":
            buttons[index].config(fg="black")  # X player color
        else:
            buttons[index].config(fg="red")  # O player color
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn", fg="blue" if current_player == "X" else "red")

# Main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.config(bg="blue")  # Background color

# Create buttons
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in a grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

# Initial player
current_player = "X"
winner = False

# Game label
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16), bg="lightyellow", fg="blue")
label.grid(row=3, column=0, columnspan=3)

# Run the main loop
root.mainloop()
