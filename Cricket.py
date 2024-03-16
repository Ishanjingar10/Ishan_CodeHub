import random
import sys 
import csv
from tkinter import *
from tkinter import messagebox

def play_cricket_game(player_name):
    player_score = 0
    computer_score = 0

    while True:
        try:
            player_choice = int(input("Enter your choice: "))

            computer_choice = random.randint(1, 10)
            sys.stdout.write(f"Computer choice: {computer_choice}\n")

            if player_choice < 1 or player_choice > 10:
                messagebox.showerror(title="Error", message="Invalid Choice")
                continue

            if player_choice == computer_choice:
                sys.stdout.write("Out!\n")
                break
            else:
                player_score += player_choice
                computer_score += computer_choice
                sys.stdout.write("-----------------------\n")
                sys.stdout.write(f"Your score: {player_score}\n")
                sys.stdout.write(f"Computer score: {computer_score}\n")
                sys.stdout.write("-----------------------\n")

            if computer_score >= 100 or player_score >= 100:
                break

        except ValueError:
            messagebox.showerror(title="Error", message="Invalid Choice! Enter a number between 1 and 10.")

    sys.stdout.write("Game over!\n")
    sys.stdout.write("-----------------------\n")
    sys.stdout.write("------Final Score------\n")
    sys.stdout.write(f"Your score: {player_score}\n")
    sys.stdout.write(f"Computer score: {computer_score}\n")
    sys.stdout.write("-----------------------\n")

    if player_score > computer_score:
        sys.stdout.write("Player Won and Computer Lost!\n")
    elif player_score == computer_score:
        sys.stdout.write("You and Computer had the same score!\n It's a TIE!\n")
    else:
        sys.stdout.write("Computer Won and You lost!\n")

    return player_score, computer_score

def on_okay():
    name = entry_name.get()
    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return

    messagebox.showinfo("Welcome", f"Welcome, {name}!\nLet's play Hand Cricket!")

    player_score, computer_score = play_cricket_game(name)

    with open("handCric.csv", "a", newline='') as f1:
        writer1 = csv.writer(f1)
        writer1.writerow([name, player_score, computer_score])

    entry_name.delete(0, 'end')  # Clear the entry for the next player

    ask = messagebox.askquestion("Play Again", "Do you want to play again?")
    if ask == "yes":
        on_okay()
    else:
        messagebox.showinfo("Game Ended", "THANK YOU FOR PLAYING")
        window.destroy()

window = Tk()
window.title("Hand Cricket Game")

# Label and entry for player's name
label_name = Label(window, text="Enter your name:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = Entry(window)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Button to start the game
button_okay = Button(window, text="Okay", command=on_okay)
button_okay.grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()
