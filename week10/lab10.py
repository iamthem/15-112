# Leandro Lopez
# lslopez, rboppana (groupmate)
# Section H 
# Lab 10

import cs112_f17_week10_linter
import os 
from tkinter import * 
import math 

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

###################
# Problems 
###################


def helperFindLargestFile(path):
    if os.path.isfile(path): #Return size of file path is file 
        return os.path.getsize(path), path
    elif os.path.isdir(path):
        if len(os.listdir(path)) == 0: return 0, ""
        else:
            largest = 0, ''
            for item in os.listdir(path):
                if (helperFindLargestFile(os.path.join(path, item))[0] 
                        > largest[0]):
                    largest = helperFindLargestFile(os.path.join(path, item))
            return largest

def findLargestFile(path):
    result = helperFindLargestFile(path)
    return result[-1] 

def checkBoard(board):
    for row in board:
        if 0 in row: return False
    return True

def solveSudoku(board):
    if checkBoard(board): return board
    else: 
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == 0:
                    for digit in range(1,10):
                        board[row][col] = digit
                        if isLegalSudoku(board):
                            solution = solveSudoku(board)
                            if solution != None: 
                                return solution 
                        board[row][col] = 0
                    return None 
                            
######################
# Ignore Rest 
######################

def init(data): 
    data.level = 1

def teddyFace(canvas, x, y, r):
    tan = "#%02x%02x%02x" % (209, 180, 140)
    canvas.create_oval(x-r, y-r, x+r, r+y, width=r/10, fill="brown")
    canvas.create_oval(x-r/2.25, y-r/10, x+r/2.25, y-r/10+r/1.1,
            width=r/15, fill=tan)
    for i,j in [(0,0), (r/3, r/2.2) , (-1*r/3, 1*r/2.2)]:
        canvas.create_oval((x+i)-r/7, (y+r/5-j)-r/7, 
                (x+i)+r/7, r/7+(y+r/5-j), fill='black')

def fractalTeddy(canvas, x, y, r, level):
    #(x,y) is the center of the circle 
    if level == 0: 
        teddyFace(canvas, x, y, r)
    else:
        fractalTeddy(canvas, x, y, r, level-1)
        fractalTeddy(canvas, x+r, y-r, r/2, level-1)
        fractalTeddy(canvas, x-r, y-r, r/2, level-1)

def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

def redrawAll(canvas, data):
    fractalTeddy(canvas, 250, 250, 100, data.level)
    canvas.create_text(250, 25,
                       text = "Level %d Teddy Bear" % (data.level),
                       font = "Arial 26 bold")
    canvas.create_rectangle(250, 50,
                       text = "Use arrows to change level",
                       font = "Arial 10")
   
def areLegalValues(values):
  if math.sqrt(len(values)) % 1 != 0: return False
  else:
    for i in range(len(values)):
      if (values[i] >= 0) and (values[i] <= len(values)):
        if values[i] == 0: continue
        else:
          for j in range(len(values)):
            if j == i: continue
            elif values[i] == values[j]: return False
      else: return False
  return True



def isLegalRow(board, row):
  return areLegalValues(board[row])
  
def isLegalCol(board, col):
  colList = []
  for i in range(len(board)):
    colList += [board[i][col]]
  return areLegalValues(colList)

def isLegalBlock(board, block):
  blockLen = int(math.sqrt(len(board)))
  blockList = []
  a = (block//blockLen)*blockLen
  b = (block%blockLen)*blockLen
  for i in range(blockLen):
    blockList += board[i+a][b:b+blockLen]
  print(blockList)
  return areLegalValues(blockList)

def isLegalSudoku(board):
  n = math.sqrt(len(board))
  if n % 1 != 0: return False
  else:
    for i in range(len(board)):
      if (isLegalRow(board, i)): continue
      else: return False
    for i in range(len(board)):
      if (isLegalCol(board, i)): continue
      else: return False
    for i in range(len(board)):
      if (isLegalBlock(board, i)): continue
      else: return False
  return True

###########
# Use Run as-is
###########
def run(width=400, height=400):
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
    data.timerDelay = 100 # milliseconds
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

def runTeddyFractalViewer():
    run(500,500)

def main():
    cs112_f17_week10_linter.lint()

if __name__ == '__main__':
    main()
