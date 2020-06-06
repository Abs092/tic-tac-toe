import tkinter as tk
import tkinter.font as font
import tkinter.messagebox as msgbox
import random
import TicTacToeAI

# After the Click of any button
def AfterClickButton(i,j):
    global turn
    global data
    currentButton = Buttons[0][0]
    
    # if it is computer's turn then i and j value are -1. For user it is based on selection.
    if(i != -1):
        currentButton = Buttons[i][j]

    if (i == -1 or currentButton['text'] == ""):
        # check that it is user selection and user is selected empty button.
        if ( turn == 0 and i != -1 and j != -1):
            # Set "X" on clicked button.
            currentButton.config(text = "X")
            turn = 1
            data[i][j] = 1
            # Check that user is win or not. 
            if(TicTacToeAI.CheckWin(data,1)) :
                result = msgbox.askyesno("Player 1 Win" ,"Do you want to continue ?")
                if(result):
                    RestartGame()
                else :
                    DistroyGame()
            # If there is no possible move left then ask to restart.
            elif(not TicTacToeAI.AnyEmptySpace(data)) :
                result = msgbox.askyesno("Match Draw" ,"Do you want to continue ?")
                if(result):
                    RestartGame()
                else :
                    DistroyGame()
            # Menually call computer move.
            else :
                AfterClickButton(-1,-1)
                
        else :
            # try to compute move for computer. 
            move = TicTacToeAI.getComputerMove(data)
            TicTacToeAI.MakeMove(data,move[0],move[1],2)
            currentButton = Buttons[move[0]][move[1]]
            currentButton.config(text = "0")
            turn = 0
            # check that computer is win or not.
            if(TicTacToeAI.CheckWin(data,2)) :
                result = msgbox.askyesno("Player 2 Win" ,"Do you want to continue ?")
                if(result):
                    RestartGame()
                else :
                    DistroyGame()
            # If there is no possible move left then ask to restart.
            elif(not TicTacToeAI.AnyEmptySpace(data)):
                result = msgbox.askyesno("Match Draw" ,"Do you want to continue ?")
                if(result):
                    RestartGame()
                else :
                    DistroyGame()

# After the complitation of game if user want to play more then restart the game.            
def RestartGame():
    global data
    global Buttons
    global turn
    turn = 0 
    for i in range(0,3):
        for j in range(0,3):
            data[i][j] = 0

    for layer in Buttons:
        for button in layer :
            button.config(text = "")

# Close the window ...
def DistroyGame():
    global window
    window.destroy()

# OnClick of button 9.        
def Button1Click():
    AfterClickButton(0,0)

# OnClick of button 9.
def Button2Click():
    AfterClickButton(0,1)

# OnClick of button 9.    
def Button3Click():
    AfterClickButton(0,2)

# OnClick of button 9.
def Button4Click():
    AfterClickButton(1,0)

# OnClick of button 9.
def Button5Click():
    AfterClickButton(1,1)

# OnClick of button 9.
def Button6Click():
    AfterClickButton(1,2)

# OnClick of button 9.
def Button7Click():
    AfterClickButton(2,0)

# OnClick of button 9.
def Button8Click():
    AfterClickButton(2,1)

# OnClick of button 9.
def Button9Click():
    AfterClickButton(2,2)

window = tk.Tk()
window.title("Tic Tac Toe")

turn = 0 # 0 indicates player turn.

data = [[0,0,0],[0,0,0],[0,0,0]]
TopLayerButtons = []
MiddleLayerButtons = []
BottomLayerButtons = []

Buttons = [TopLayerButtons , MiddleLayerButtons , BottomLayerButtons]

# Buttons for 1st layer.
TopLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button1Click))
TopLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button2Click))
TopLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button3Click))

# Buttons for second layer.
MiddleLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button4Click))
MiddleLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button5Click))
MiddleLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button6Click))

# Buttons for third layer.
BottomLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button7Click))
BottomLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button8Click))
BottomLayerButtons.append(tk.Button(window,height = 4 ,width = 6,command = Button9Click))

# Set Font and position of the button.
buttonFont = font.Font(size=30)
i = 0
for layer in Buttons:
    j = 0
    for button in layer:
        button.grid(row = i ,column = j)
        button['font'] = buttonFont
        j = j+1
    i = i + 1

window.mainloop()
