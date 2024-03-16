from tkinter import *

root = Tk()
root.geometry("300x450")
root.title("Tic Tak Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel1 = Label(frame1 , text="Tic Tak Toe" , font=("Arial" , 20) , bg="yellow")
titleLabel1.pack()

frame2 = Frame(root)
frame2.pack()

board = {1:" " , 2:" " , 3:" ",
         4:" " , 5:" " , 6:" ",
         7:" " , 8:" " , 9:" "}

turn = "X"

game_end = False

def checkForWin(player):
    #All Rows
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True
    
    #All columns
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    
    #Diagonals
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    
    return False


def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " " 
        
    for i in board.keys():
        board[i] = " "
    
    WinningLabel = Label(frame2 , text=f"                              " , font=("Arial" , 15))
    WinningLabel.grid(row = 3 , column = 0 , columnspan = 5)

#Function to play
def play(event):
    global WinningLabel
    global turn , game_end
    if game_end:
        return
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]

    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)
    
    if button["text"] == " ":
        if turn == "X":
            button["text"] = "X"
            board[clicked] = turn
            if checkForWin(turn):
                WinningLabel = Label(frame2 , text=f"{turn} wins the game!!" , font=("Arial" , 15) , bg="yellow")
                WinningLabel.grid(row = 3 , column = 0 , columnspan = 3)
                game_end = True
            turn = "O"
            
        else:
            button["text"] = "O"
            board[clicked] = turn
            if checkForWin(turn):
                WinningLabel = Label(frame2 , text=f"{turn} wins the game!!" , font=("Arial" , 15) , bg="yellow")
                WinningLabel.grid(row = 3 , column = 0 , columnspan = 3)
                game_end = True
            turn = "X"
            
        if checkForDraw():
            DrawLabel = Label(frame2 , text=f"Game Draw!!" , font=("Arial" , 15) , bg="yellow")
            DrawLabel.grid(row = 3 , column = 0 , columnspan = 3)

#Tic Tak Toe Board
#First Row

button1 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button1.grid(row = 0 , column = 0)
button1.bind("<Button-1>" , play)

button2 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button2.grid(row = 0 , column = 1)
button2.bind("<Button-1>" , play)

button3 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button3.grid(row = 0 , column = 2)
button3.bind("<Button-1>" , play)

#Second Row

button4 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button4.grid(row = 1 , column = 0)
button4.bind("<Button-1>" , play)

button5 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button5.grid(row = 1 , column = 1)
button5.bind("<Button-1>" , play)

button6 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button6.grid(row = 1 , column = 2)
button6.bind("<Button-1>" , play)

#Third Row

button7 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button7.grid(row = 2 , column = 0)
button7.bind("<Button-1>" , play)

button8 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button8.grid(row = 2 , column = 1)
button8.bind("<Button-1>" , play)

button9 = Button(frame2 , text= " " , width=4 , height=2 , font=("Arial" , 25) , bg="sky blue" , relief = RAISED , borderwidth=4)
button9.grid(row = 2 , column = 2)
button9.bind("<Button-1>" , play)

RestartButton = Button(frame2 , text = "Restart Game" , width = 12 , height = 1 , font=("Arial" , 15) , bg = "Light Green", relief = RAISED , borderwidth=4 , command = restartGame) 
RestartButton.grid(row = 4 , column = 0 , columnspan = 3)

buttons = [button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8 , button9]

root.mainloop()