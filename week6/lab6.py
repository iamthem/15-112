# Leandro Lopez

# lslopez, mkchan, xuliangs (groupmates)

# Section H

##############
# Lab 6
##############
from tkinter import *
import random 
import copy
####################################
# customize these functions
####################################

def init(data):
    data.cols = 15 
    data.isGameOver = False
    data.rows = 10 
    data.cellsize = 20
    data.margin = 30
    data.emptycolor = 'blue'
    data.board = [ ([data.emptycolor]* data.cols) for i in range(data.rows)]

    # Seven "standard" pieces (tetrominoes)

    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]

    data.tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    data.tetrisPieceColors = ["red", "yellow", "magenta", "pink", "cyan", "green", "orange"]
    
    data.fallingPiece = []
    data.fallingPieceColor = []
    data.fallingPieceRow = 0
    data.fallingPieceCol = 0 
    data.score = 0 

    if not data.isGameOver:
       newFallingPiece(data)

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if (event.keysym == "Left"): moveFallingPiece(data, 0, -1) 
    elif (event.keysym == "Right"): moveFallingPiece(data, 0, +1)  
    elif (event.keysym == "Up"): rotateFallingPiece(data) 
    elif (event.keysym == "Down"): moveFallingPiece(data, +1, 0)

def timerFired(data):
    if moveFallingPiece(data, +1, 0):
        moveFallingPiece(data, +1, 0)
    
    elif fallingPieceIsLegal(data):
        placeFallingPiece(data)
    
    else: 
        data.isGameOver = True

def removeFullRows(data):
    resultBoard = []
    clearRow = ['blue'] * 15
    rowsRemoved = 0
    for i in range(10):
        if data.emptycolor in data.board[i]:
            resultBoard.append(data.board[i])
        else:
            rowsRemoved += 1
    data.score += rowsRemoved ** 2
    while len(resultBoard) != len(data.board):
        resultBoard.insert(0, clearRow)
    
    data.board = resultBoard

def placeFallingPiece(data):
    for l in range(len(data.fallingPiece)):
        for i in range(len(data.fallingPiece[l])):
            if data.fallingPiece[l][i]: 
                data.board[data.fallingPieceCol + i][data.fallingPieceRow + l] = data.fallingPieceColor
    removeFullRows(data)
    if not data.isGameOver:
        newFallingPiece(data)

def rotateFallingPiece(data):
    oldList = copy.deepcopy(data.fallingPiece)
    oldRows, oldCols = len(data.fallingPiece), len(data.fallingPiece[0])
    oldCoordinateRow, oldCoordinateCol =  data.fallingPieceRow, data.fallingPieceCol 
    newRows, newCols = oldCols, oldRows
    
    newRow = (oldCoordinateRow + oldRows//2) - newRows // 2 
    newCol = (oldCoordinateCol + oldCols//2) - newCols // 2 
    
    nextRow = []
    rotatedPiece = []
    for i in range(oldCols - 1, -1, -1):
        for j in range(oldRows):
            nextRow.append(oldList[j][i])
        rotatedPiece.append(nextRow)
        nextRow = []
    
    data.fallingPiece = rotatedPiece
    data.fallingPieceRow = newRow
    data.fallingPieceCol = newCol
    
    if not fallingPieceIsLegal(data):
        data.fallingPiece = oldList
        data.fallingPieceRow = oldCoordinateRow
        data.fallingPieceCol = oldCoordinateCol

def moveFallingPiece(data, drows, dcol):
    data.fallingPieceCol += dcol 
    data.fallingPieceRow += drows
    if not fallingPieceIsLegal(data):      
        data.fallingPieceCol -= dcol 
        data.fallingPieceRow -= drows
        return False
    return True

def fallingPieceIsLegal(data):
    for l in range(len(data.fallingPiece)):
        for i in range(len(data.fallingPiece[l])):
            if data.fallingPiece[l][i]:
                if ((data.fallingPieceCol + i < 0) or 
                    (data.fallingPieceCol + i >= data.rows)):
                    return False 
                elif ((data.fallingPieceRow + l < 0) or 
                    (data.fallingPieceRow + l >= data.cols)):
                    return False
                elif data.board[data.fallingPieceCol+i][data.fallingPieceRow+l] != 'blue':
                    return False
    return True

def newFallingPiece(data):
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.fallingPiece = data.tetrisPieces[randomIndex]
    fallingPieceCols = len(data.fallingPiece[0]) 
    data.fallingPieceColor = data.tetrisPieceColors[randomIndex]
    data.fallingPieceCol = data.rows//2 - fallingPieceCols//2 
    data.fallingPieceRow = 0
 
def drawFallingPiece(canvas, data):
    for l in range(len(data.fallingPiece)):
        for i in range(len(data.fallingPiece[l])):
            if data.fallingPiece[l][i]: 
                drawCell(canvas, data, data.fallingPieceCol + i, data.fallingPieceRow + l,
                    data.fallingPieceColor)

def drawCell(canvas, data, row, col, color):
    x0, y0 = data.cellsize * row + data.margin,  data.cellsize * col + data.margin
    x1, y1 = data.cellsize * (row+1) + data.margin,  data.cellsize * (col+1) + data.margin
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, width="3")

def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col, data.board[row][col])

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0,0, data.width, data.height, fill='orange')
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    if data.isGameOver:
        canvas.create_text(data.width//2, data.height//4, fill="purple", 
                text="GAME OVER", font = 'Calibri 20 bold')
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 1000 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

def playTetris():
    margin, rows, cols, cellSize = 30, 10, 15, 20
    run(260, 375)
