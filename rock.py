import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def play():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(['r', 'p', 's'])
    
    result = get_result(user_choice, computer_choice)
    display_result(result, computer_choice)
    highlight_winner(result)

def get_result(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'r' and computer == 's') or \
         (player == 's' and computer == 'p') or \
         (player == 'p' and computer == 'r'):
        return "win"
    else:
        return "lose"

def display_result(result, computer_choice):
    if result == "tie":
        result_label.config(text="It's a tie", fg="gray")
    elif result == "win":
        result_label.config(text="You won!", fg="green")
    else:
        result_label.config(text="You lost!", fg="red")
        
    computer_choice_label.config(image=choice_images[computer_choice])

def highlight_winner(result):
    for button in choice_buttons:
        button.config(bg="SystemButtonFace")
    if result == "win":
        user_choice_button = choice_buttons[user_choice_var.get()]
        user_choice_button.config(bg="lightgreen")
    elif result == "lose":
        computer_choice_button = choice_buttons[computer_choice]
        computer_choice_button.config(bg="lightgreen")

def reset_game():
    confirmed = messagebox.askyesno("Reset Game", "Are you sure you want to reset the game?")
    if confirmed:
        user_choice_var.set("")
        result_label.config(text="")
        computer_choice_label.config(image="")
        for button in choice_buttons:
            button.config(bg="SystemButtonFace")

# Create main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Load images
rock_img = Image.open("rock.png")
rock_img = rock_img.resize((100, 100), Image.BILINEAR)
rock_photo = ImageTk.PhotoImage(rock_img)

paper_img = Image.open("paper.png")
paper_img = paper_img.resize((100, 100), Image.BILINEAR)
paper_photo = ImageTk.PhotoImage(paper_img)

scissors_img = Image.open("scissors.png")
scissors_img = scissors_img.resize((100, 100), Image.BILINEAR)
scissors_photo = ImageTk.PhotoImage(scissors_img)

# Create and pack widgets
user_choice_var = tk.StringVar()
choice_buttons = {}

instructions_label = tk.Label(root, text="Choose your move:", font=("Helvetica", 14))
instructions_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))

rock_button = tk.Button(root, image=rock_photo, command=lambda: user_choice_var.set("r"))
rock_button.grid(row=1, column=0, padx=10)
choice_buttons["r"] = rock_button

paper_button = tk.Button(root, image=paper_photo, command=lambda: user_choice_var.set("p"))
paper_button.grid(row=1, column=1, padx=10)
choice_buttons["p"] = paper_button

scissors_button = tk.Button(root, image=scissors_photo, command=lambda: user_choice_var.set("s"))
scissors_button.grid(row=1, column=2, padx=10)
choice_buttons["s"] = scissors_button

play_button = tk.Button(root, text="Play", font=("Helvetica", 12), command=play)
play_button.grid(row=2, column=0, columnspan=3, pady=(10, 5))

result_label = tk.Label(root, font=("Helvetica", 14))
result_label.grid(row=3, column=0, columnspan=3)

computer_choice_label = tk.Label(root)
computer_choice_label.grid(row=4, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3, pady=(10, 20))

# Dictionary to map computer's choice to corresponding image
choice_images = {
    "r": rock_photo,
    "p": paper_photo,
    "s": scissors_photo
}

# Run the main event loop
root.mainloop()
