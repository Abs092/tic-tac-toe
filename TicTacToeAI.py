import random

def getBoardCopy(data):
    # Make a duplicate of the board list and return it the duplicate.
    newData = [[],[],[]]
    k = 0
    for i in data:
        for j in i:
            newData[k].append(j)
        k = k + 1

    return newData


def getComputerMove(data):
    # Given a board and the computer's letter, determine where to move and return that move.
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(0, 3):
        for j in range(0,3):
            copy = getBoardCopy(data)
            if IsEmptySpace(copy, i ,j):
                print ("Try to check win at (" + str(i) + "," +str(j) +")" )
                MakeMove(copy, i ,j,2)
                if CheckWin(copy, 2):
                    return (i,j)

    # Check if the player could win on his next move, and block them.
    for i in range(0, 3):
        for j in range(0,3):
            copy = getBoardCopy(data)
            if IsEmptySpace(copy, i,j):
                MakeMove(copy, i, j,1)
                print ("Try to check player is not win at (" + str(i) + "," +str(j) +")" )
                if CheckWin(copy, 1):
                    return (i,j)

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(data, [(0,0), (0,2), (2,0), (2,2)])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if IsEmptySpace(data, 1,1):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(data, [(0,1), (1,0), (1,2), (2,1)])

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if IsEmptySpace(board, i[0],i[1]):
            possibleMoves.append((i[0],i[1]))

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def IsEmptySpace(data,i,j):
    if(data[i][j] == 0) :return True

def MakeMove(data,i,j,fillValue):
    data[i][j] = fillValue
def AnyEmptySpace(data) :
    for i in range(0,3):
        for j in range(0,3):
            if(data[i][j] == 0):
                return True
    return False

def CheckWin(data,le):
    if ((data[0][0] == le and data[0][1] == le and data[0][2] == le) or # across the top
    (data[1][0] == le and data[1][1] == le and data[1][2] == le) or # across the middle
    (data[2][0] == le and data[2][1] == le and data[2][2] == le) or # across the bottom
    (data[0][0] == le and data[1][0] == le and data[2][0] == le) or # down the left side
    (data[0][1] == le and data[1][1] == le and data[2][1] == le) or # down the middle
    (data[0][2] == le and data[1][2] == le and data[2][2] == le) or # down the right side
    (data[0][0] == le and data[1][1] == le and data[2][2] == le) or # diagonal 
    (data[0][2] == le and data[1][1] == le and data[2][0] == le)) :
        return True
