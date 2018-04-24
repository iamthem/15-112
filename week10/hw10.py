# Leandro Lopez
# lslopez
# Section H 
# HW 10

import cs112_f17_week10_linter
from tkinter import * 
import math 
from copy import deepcopy 

###################
# Problems 
###################

def flattenHelper(L, elements = []): #Recursive helper 
    for element in L: #If element is list, call function else add it to results
        if isinstance(element, list): flattenHelper(element, elements)
        else: elements.append(element)
    return elements 

def flatten(L): #Wrapper funciton 
    if not isinstance(L, list): return L  #If not a list return element
    else:
        a = flattenHelper(L)          #call answer 
        tmp = deepcopy(a)             #copy answer 
        del a[:]                      #reset elements to []
        return tmp                    # return copy 

def noError(f): 
    def wrapper(*args):             #*args adjusts for arbitrary arguments
        try: 
            return f(*args)         #If function doesn't crash, return result
        except:
            return None             #If it crashes return None
    return wrapper                  #Return new function 

def getConstraints(constraints):            #Get constraints in list form
    diag1 = constraints[0], constraints[12] #Get first diagonal 
    diag2 = constraints[6], constraints[18] #Get second diagonal
    rowCons, colCons = [], [] 
    topRow, botRow, leftCol, rightCol = [], [], [], []
    for i in range(23,18, -1): #Get top row
        topRow.append(constraints[i])
    for i in range(7, 12):     #Get bottom row 
        botRow.append(constraints[i])
    for i in range(1, 6):      # Get left column
        leftCol.append(constraints[i])
    for i in range(17,12,-1):  # Get right column 
        rightCol.append(constraints[i])
    for i in range(5):         # Combine to get all constraints  
        rowCons.append((topRow[i], botRow[i])) 
        colCons.append((leftCol[i], rightCol[i]))
    return rowCons, colCons, diag1, diag2

def checkConstraints(board, constraints, aLocation):
    #Get constraints 
    rowCons, colCons, diag1, diag2 = getConstraints(constraints)
    for i in range(5):
        for j in range(5): #Iterate through board
            #If board cell is A, chech indices are correct 
            if board[i][j] == 'A' and i == aLocation[0] and j == aLocation[1]:
                continue
            #If cell is empty, continue to next iteration 
            elif board[i][j] == '': continue
            #If cell is in row constraints, continue iterating and cross it 
            #out of pool of letters 
            elif board[i][j] in rowCons[i]:
                rowCons[i] = tuple(set(rowCons[i]) - set(board[i][j]))
            #If cell is in col constraints, continue iterating and cross it 
            #out of pool of letters 
            elif board[i][j] in colCons[j]: 
                colCons[j] = tuple(set(colCons[j]) - set(board[i][j]))
            #If cell is in diag1 constraints, continue iterating and cross it 
            #out of pool of letters 
            elif board[i][j] in diag1 and i == j:
                diag1 = tuple(set(diag1) - set(board[i][j]))
            #If cell is in diag2 constraints, continue iterating and cross it 
            #out of pool of letters 
            elif board[i][j] in diag2 and i+j == 4:
                diag2 = tuple(set(diag2) - set(board[i][j]))
            else: return False
    return True

# Make a 5x5 board with the A at the correct location 
def makeBoard(aLocation):
    board = [([''] * 5) for row in range(5)]
    board[aLocation[0]][aLocation[1]] = 'A'
    return board

# Make board and call recursive function 
def solveABC(constraints, aLocation):
    board = makeBoard(aLocation)
    return recursiveABC(board, aLocation, constraints, aLocation)

# Check if board is solved 
def isSolved(board):
    for row in board:
        if '' in row: return False
    return True

def recursiveABC(board, currLocation, constraints, aLocation):
    if isSolved(board): return board                #Base case 
    else:
        # Get constraints 
        rowCons, colCons, diag1, diag2 = getConstraints(constraints)
        # Generate matrix with possible moves 
        deltas = [(i,j) for i in (-1,0,1) for j in (-1,0,1) 
                   if not (i == j == 0)]
        # Assign currect location to i and j indices 
        i,j = currLocation[0], currLocation[1]
        # For each move in the matrix
        for dx, dy in deltas:
            # check if move is legal and cell is empty
            if ((0 <= (i+dx) < 5 and 0 <= (j+dy) < 5) and 
                (board[i+dx][j+dy] == '')):
                # Try each letter that could go here from constraints
                for letter in rowCons[i+dx]+colCons[j+dy]+diag1+diag2:
                        board[i+dx][j+dy] = letter
                        # Check if letter follows alphabetically from 
                        # previous letter and agrees with constraints 
                        if ((ord(letter)-1 == ord(board[i][j])) and 
                            (checkConstraints(board, constraints, aLocation))):
                                solution = recursiveABC(board, 
                                        (i+dx, j+dy), constraints, aLocation)
                                # Return solution if correct 
                                if solution != None: 
                                    return solution
                board[i+dx][j+dy] = '' #If letter doesn't work make empty cell
        return None               #If conditions aren't satisfied return None


######################
# Ignore Rest 
######################

def init(data):
    data.level = 0 #Start at level 0
    
def drawH(canvas, x0, y0, w, h): #Draw H with given parameters
    canvas.create_line(x0, y0, x0+w, y0, width=4)
    canvas.create_line(x0, y0+h, x0, y0-h, width=4)
    canvas.create_line(x0+w, y0+h, x0+w, y0-h, width=4)


def drawFractalH(canvas, x0, y0, w, h, level):
    if level == 0: #Base case, draw H
        drawH(canvas, x0, y0, w, h)
    else: #Recursive step, draw 5 H's 
        drawFractalH(canvas, x0, y0, w, h, level-1)
        drawFractalH(canvas, x0 - w/4, y0 + h, w/2, h/2, level-1)
        drawFractalH(canvas, x0 - w/4, y0 - h, w/2, h/2, level-1)
        drawFractalH(canvas, x0 + 3*w/4, y0 + h, w/2, h/2, level-1)
        drawFractalH(canvas, x0 + 3*w/4, y0 - h, w/2, h/2, level-1)
    
# If user presses keys change level
def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

# Draw fractals recursively 
def redrawAll(canvas, data):
    drawFractalH(canvas, 125, data.height/2, data.width/2, data.height/4, 
        data.level) 

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

def hFractal(): # Draw fractal
    run(500,500)

##############
# Test Functions 
###############
def testFlatten():
    print('Testing flatten()...', end='')
    assert(flatten([1,[2]]) == [1,2])
    assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
    assert(flatten(['wow', [2,[[]]], [True]]) == ['wow', 2, True])
    assert(flatten([]) == [])
    assert(flatten(3) == 3)
    assert(flatten([['a',42,'test'],True,'',[]]) == ['a',42,'test',True,''])
    assert(flatten([[[]], (), set()]) == [(), set()])
    assert(flatten([[[{1:'a'}], 2], (), set()]) == [{1: 'a'}, 2, (), set()])
    print('Done!')

def testNoErrorDecorator():
    print("Testing @noError decorator...", end="")
    @noError
    def f(x, y): return x/y
    assert(f(1, 5) == 1/5)
    assert(f(1, 0) == None)

    @noError
    def g(): return 1/0
    assert(g() == None)

    @noError
    def h(n):
        if (n == 0): return 1
        else: return h(n+1)
    assert(h(0) == 1)
    assert(h(-1) == 1)
    assert(h(1) == None)

    print("Passed!")

def testSolveABC():
    print("Testing solveABC()...", end="")
    constraints = "CHJXBOVLFNURGPEKWTSQDYMI"
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['I', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'B', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'Q', 'P']
               ]
    assert(board == solution)
    constraints = 'JVOKFDRCXWGTNIHQMYLUSEBP'
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['Y', 'O', 'P', 'C', 'A'],
                ['X', 'N', 'Q', 'B', 'D'],
                ['W', 'M', 'R', 'F', 'E'],
                ['V', 'L', 'S', 'J', 'G'],
                ['U', 'T', 'K', 'H', 'I']
                ]
    assert(board == solution)
    constraints = 'XGCJLMFTWDNIYROEVBSKHQPU'
    aLocation = (1,0)
    board = solveABC(constraints, aLocation)
    solution = [['Y', 'V', 'U', 'T', 'S'],
                ['A', 'X', 'W', 'P', 'R'],
                ['B', 'C', 'D', 'O', 'Q'],
                ['H', 'F', 'E', 'L', 'N'],
                ['G', 'I', 'J', 'K', 'M']
            ]
    assert(board == solution)
    print('Passed!')
    aLocation = (1,2)
    board = solveABC(constraints, aLocation)
    assert(board == None)
def testAll():
    testFlatten()
    testNoErrorDecorator()
    testSolveABC()

def main():
    cs112_f17_week10_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
