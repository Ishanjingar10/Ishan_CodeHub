# Ishan_CodeHub
**Hand Cricket Game!!**

It is a Python program for a simple hand cricket game implemented using the Tkinter library for the graphical user interface (GUI).

1. **Imports**: The code begins with importing necessary modules such as `random`, `sys`, `csv`, and `Tkinter`.

2. **`play_cricket_game` Function**: This function defines the core logic of the hand cricket game. It takes the player's name as input and lets the player play the game against the computer. The player and computer take turns selecting numbers between 1 and 10. If the player's choice matches the computer's choice, the player is considered "Out." The game continues until the player is out or until either the player or the computer reaches a score of 100. After the game ends, the function returns the player's and computer's scores.

3. **`on_okay` Function**: This function is triggered when the player clicks the "Okay" button on the GUI. It retrieves the player's name from the entry widget. If no name is entered, it prompts the user to enter a name. If a name is entered, it displays a welcome message and starts the game by calling the `play_cricket_game` function. After the game ends, it writes the player's name and scores to a CSV file named "handCric.csv". It then prompts the player if they want to play again. If the player chooses to play again, the function recursively calls itself; otherwise, it displays a "Game Ended" message and closes the GUI window.

4. **GUI Setup**: The code sets up a Tkinter window titled "Hand Cricket Game." It includes a label and an entry widget for the player to enter their name. There's also a button labeled "Okay" that triggers the `on_okay` function when clicked.

5. **Main Loop**: The `window.mainloop()` function starts the Tkinter event loop, allowing the GUI to interact with the user.

Overall, this code combines Python's core functionalities with Tkinter's GUI capabilities to create a simple interactive hand cricket game where players can compete against a computer opponent.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**QR Code!!**

It generates a QR code using the qrcode library in Python.

Import: The code imports the qrcode module and renames it to qr for convenience.

QR Code Generation: The qr.make() function is used to generate a QR code. It takes a string argument representing the data to be encoded into the QR code. In this case, the string is a Google Maps link: "https://maps.app.goo.gl/t7ZxYX1cnUWi8q3m8".

Saving the QR Code: The generated QR code image is then saved to a file named "Sarvodaya_Charm_Udhyog_Bhandar.png" using the img.save() method.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


**Tic Tak Toe Game!!**

It is a simple implementation of the Tic Tac Toe game using the Tkinter library in Python. Here's a brief description:

1. **Tkinter Setup**: The code starts by importing the necessary modules from Tkinter and creating the root window with the specified dimensions and title.

2. **Game Logic**: The game logic is implemented using a dictionary `board` to represent the Tic Tac Toe board, where keys represent board positions and values represent the current state (either "X" or "O"). The `turn` variable keeps track of whose turn it is ("X" or "O"). There's also a `game_end` variable to track if the game has ended.

3. **Winning and Draw Check**: Functions `checkForWin()` and `checkForDraw()` are defined to check for a winning condition or a draw.

4. **Restart Game Function**: The `restartGame()` function resets the game state when the "Restart Game" button is clicked.

5. **Play Function**: The `play()` function is called when a button on the game grid is clicked. It updates the button text based on the current player's turn and updates the board state accordingly. It also checks for a win or draw condition after each move.

6. **Tic Tac Toe Board**: The Tic Tac Toe grid is created using Tkinter buttons arranged in a 3x3 grid layout. Each button is configured to call the `play()` function when clicked.

7. **Restart Button**: A "Restart Game" button is provided to allow players to restart the game.

8. **Main Loop**: The `root.mainloop()` function starts the Tkinter event loop, allowing the GUI to interact with the user.
