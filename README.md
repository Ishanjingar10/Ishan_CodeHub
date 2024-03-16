# Ishan_CodeHub
**Hand Cricket Game**

Certainly! The provided code is a Python program for a simple hand cricket game implemented using the Tkinter library for the graphical user interface (GUI). Here's a brief description of the code:

1. **Imports**: The code begins with importing necessary modules such as `random`, `sys`, `csv`, and `Tkinter` (renamed to `Tk` for convenience).

2. **`play_cricket_game` Function**: This function defines the core logic of the hand cricket game. It takes the player's name as input and lets the player play the game against the computer. The player and computer take turns selecting numbers between 1 and 10. If the player's choice matches the computer's choice, the player is considered "Out." The game continues until the player is out or until either the player or the computer reaches a score of 100. After the game ends, the function returns the player's and computer's scores.

3. **`on_okay` Function**: This function is triggered when the player clicks the "Okay" button on the GUI. It retrieves the player's name from the entry widget. If no name is entered, it prompts the user to enter a name. If a name is entered, it displays a welcome message and starts the game by calling the `play_cricket_game` function. After the game ends, it writes the player's name and scores to a CSV file named "handCric.csv". It then prompts the player if they want to play again. If the player chooses to play again, the function recursively calls itself; otherwise, it displays a "Game Ended" message and closes the GUI window.

4. **GUI Setup**: The code sets up a Tkinter window titled "Hand Cricket Game." It includes a label and an entry widget for the player to enter their name. There's also a button labeled "Okay" that triggers the `on_okay` function when clicked.

5. **Main Loop**: The `window.mainloop()` function starts the Tkinter event loop, allowing the GUI to interact with the user.

Overall, this code combines Python's core functionalities with Tkinter's GUI capabilities to create a simple interactive hand cricket game where players can compete against a computer opponent.
