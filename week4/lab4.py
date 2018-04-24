# Leandro Lopez
# lslopez
# Section H

#################################################
# Lab4
#################################################

import cs112_f17_week4_linter
import math, string, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

# eliminate duplicates from list d
def removeDuplicates(d):
    result = []
    for i in d:
        if i not in result:
            result.append(i)
    return result

# Check that all letters in puzzle are also in solution
def checkLetters(puzzle, solution):
    for c in puzzle: 
        if (c.isalpha()) and (c not in solution):
            return False
    return True

# Replace the letters with their assigned number values in solution 
def addLetters(s, solution):
    numList = []
    for i in s:
        if i in solution:
            numList.append(str(solution.index(i)))
    num = int(''.join(numList))
    return num

#################################################
# Problems
#################################################

def lookAndSay(a):
    b = []
    # copy a to avoid aliasing
    aCopy = copy.copy(a)

    # append a tuple (count, element) to new list b 
    for i in range(len(aCopy)):
        b.append((aCopy.count(aCopy[i]), aCopy[i]))
    
    # remove duplicates from the list b
    result = removeDuplicates(copy.copy(b))
    return result

def inverseLookAndSay(a):
    b = []
    # copy a to avoid aliasing
    aCopy = copy.copy(a)

    # For tuples (i, j), in aCopy, append j, i times into b
    for i, j in aCopy:
        for k in range(i):
            b.append(j)
    return b

def solvesCryptarithm(puzzle, solution):
    # check if all letters in puzzle are in solution
    if checkLetters(puzzle, solution):
        
        # Split the string into the addition part and answer
        addition = puzzle.split('=')[0]
        answer = puzzle.split('=')[-1]
        
        # Find the numerical representation of addition terms and answer
        firstTerm = addLetters(addition.split('+')[0],solution)
        secondTerm = addLetters(addition.split('+')[-1],solution)
        answer = addLetters(answer, solution)

        # Check if numbers add up 
        return (firstTerm + secondTerm == answer)
    return False
######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def drawStar(canvas, centerX, centerY, diameter, numPoints, color):
    angle = math.pi/2
    bigR = diameter / 2
    
    # make small circle 3/8 of the size of big circle 
    smallR = bigR * (3/8)
    
    # initialize list with tuples
    points = []

    # 2n vertices must be drawn
    for i in range(2 * numPoints):
        
        # if counter is even, put vertex at length bigR 
        if i % 2 == 0: 
            point = (centerX + bigR*math.cos(angle),
                     centerY - bigR*math.sin(angle))
            points.append(point)

       # if counter is odd, put vertex at length smallR
        else:
            point = (centerX + smallR*math.cos(angle),
                     centerY - smallR*math.sin(angle))
            points.append(point)
        
        # Add pi/n to the angle to rotate counterclockwise
        angle += math.pi/numPoints

    # display star
    canvas.create_polygon(points, fill=color)

def drawStarHelper(centerX, centerY, diameter, numPoints, color, 
                   winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    drawStar(canvas, centerX, centerY, diameter, numPoints, color)

    root.mainloop()


def drawUnitedStatesFlag(winWidth=950, winHeight=500):
  
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    
    # Draw stripes 
    for i in range(13):
        begin = winHeight*i/13
        end = winHeight*(i+1)/13
        if i%2 == 0:
            canvas.create_rectangle(0,begin,winWidth, end, fill = 'darkred', 
            width = 0)
        else:
            canvas.create_rectangle(0,begin,winWidth, end, fill = 'white', 
            width = 0)
    
    # Draw canton
    canvas.create_rectangle(0,0,winWidth/2.5,
            winHeight*7/13, fill = "navyblue",  width = 0)
    
    recWidth = winWidth/2.5
    recHeight = winHeight*7/13
    

    # Draw stars
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,winHeight*1/26, \
        winHeight*4/(5*13), 5, "white")
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,\
        winHeight/9 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(5):
        drawStar(canvas,recWidth/6 + recWidth*i/6,\
        winHeight/18 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,\
        winHeight*2/9 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(5):
        drawStar(canvas,recWidth/6 + recWidth*i/6,\
        winHeight*3/18 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,\
        winHeight*3/9 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(5):
        drawStar(canvas,recWidth/6 + recWidth*i/6,\
        winHeight*5/18 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,\
        winHeight*4/9 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(5):
        drawStar(canvas,recWidth/6 + recWidth*i/6,\
        winHeight*7/18 + winHeight*1/26, winHeight*4/(5*13), 5, "white")

    root.mainloop()


def testDrawStar():
    print("Testing drawStar()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawStarHelper(250, 250, 500, 5, "gold")
    drawStarHelper(300, 400, 100, 4, "blue")
    drawStarHelper(300, 200, 300, 9, "red")
    print("Done!")

def testDrawUnitedStatesFlag():
    print("Testing drawUnitedStatesFlag()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawUnitedStatesFlag()
    drawUnitedStatesFlag(winWidth=570, winHeight=300)
    print("Done!")

#################################################
# Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER+NUMBER=PUZZLE", "UMNZP-BLER"))
    assert(solvesCryptarithm("TILES+PUZZLES=PICTURE", "UISPELCZRT"))
    assert(solvesCryptarithm("COCA+COLA=OASIS", "LOS---A-CI"))
    assert(solvesCryptarithm("CROSS+ROADS=DANGER", "-DOSEARGNC"))

    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS") == False)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolvesCryptarithm()
    testDrawStar()
    testDrawUnitedStatesFlag()

def main():
    cs112_f17_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
