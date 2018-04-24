# Leandro Lopez
# lslopez
# Section H

#################
# HW 5
#################
import cs112_f17_week5_linter
from tkinter import *
from sudoku import *
import copy
#########################################################
# Customize these functions
# You will need to write many many helper functions, too.
#########################################################

# Initialize variables
def init(data):
    data.rows = 9
    data.cols = 9
    data.margin = 0
    data.row = 0
    data.col = 0
    data.selection = 0, 0
    data.original = copy.deepcopy(data.board)

# get bounds for cells
def getCellBounds(row, col, data):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    columnWidth = gridWidth / data.cols
    rowHeight = gridHeight / data.rows
    x0 = data.margin + col * columnWidth
    x1 = data.margin + (col+1) * columnWidth
    y0 = data.margin + row * rowHeight
    y1 = data.margin + (row+1) * rowHeight
    return (x0, y0, x1, y1)

# Put numbers on the grid
def drawNumbers(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            # get coordinates to draw grid on
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            # check if number was on the initial grid
            if data.board[row][col] != 0:
                if data.board[row][col] == data.original[row][col]:
                    canvas.create_text((x0+x1)/2, (y0+y1)/2,
                               text=str(data.board[row][col]), fill='red')
                else:
                    canvas.create_text((x0+x1)/2, (y0+y1)/2,
                            text=str(data.board[row][col]), fill='blue')

# Respond to different keys
def keyPressed(event, data, canvas):
    if (event.keysym == "Left"): data.row -= 1
    elif (event.keysym == "Right"): data.row += 1
    elif (event.keysym == "Up"): data.col -= 1
    elif (event.keysym == "Down"): data.col += 1
    elif (event.keysym == "BackSpace"):
        data.board[data.col][data.row] = 0
    # check if input is a digit
    elif (event.keysym.isdigit()):
        digit = int(event.keysym)
        # Only edit if spot is empty
        if data.board[data.col][data.row] == 0:
            data.board[data.col][data.row] = digit
        # Only edit if move is legal
        if not isLegalSudoku(data.board):
            data.board[data.col][data.row] = 0
    data.selection = data.col % 9, data.row % 9

# draw initial board
def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            fill = "orange" if (data.selection == (row, col)) else "cyan"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)

# display victory text
def drawVictory(canvas, data):
    canvas.create_text(data.width/2, data.width/2, text="You have won!",
                       fill="purple", font="Helvetica 30 bold underline")

# check if game has been won
def checkBoard(data):
    for row in data.board:
        if 0 in row: return True
    return False

# main redraw function
def redrawAll(canvas, data):
    # if game hasn't been won, keep playing
    if checkBoard(data):
        # draw grid of cells
        drawBoard(canvas, data)
        # draw numbers in board
        drawNumbers(canvas, data)
    # display victory text if game was won
    else: drawVictory(canvas, data)
########################################
# Do not modify the playSudoku function.
########################################

def playSudoku(sudokuBoard, width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data, canvas)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.board = sudokuBoard

    # Initialize any other things you want to store in data
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    # Draw the initial screen
    redrawAll(canvas, data, sudokuBoard)

    # Start the event loop
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    cs112_f17_week5_linter.lint() # check style rules

    board = [
[1,2,3,4,5,6,7,8,9],
[5,0,8,1,3,9,6,2,4],
[4,9,6,8,7,2,1,5,3],
[9,5,2,3,8,1,4,6,7],
[6,4,1,2,9,7,8,3,5],
[3,8,7,5,6,4,0,9,1],
[7,1,9,6,2,3,5,4,8],
[8,6,4,9,1,5,3,7,2],
[2,3,5,7,4,8,9,1,6]
    ]

    playSudoku(board)

if __name__ == '__main__':
    main()
