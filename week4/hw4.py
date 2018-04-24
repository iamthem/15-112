#################################################
# Hw4
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

# eliminate white lines 
def ridBlankLines(lines):
    noWhites = []
    for i in range(len(lines)):
        if (lines[i]) and (not lines[i].isspace()):
            noWhites.append(lines[i])   
    return noWhites

# Make words that are in the dictionary using a given hand
def makeWords(hand, dictionary):
    word = ''
    words = [] 
     
    # If character is in dictionary word, add it to word, else delete word
    for i in dictionary:
        for j in i:
            if j in hand and (hand.count(j) > word.count(j)): word += j
            else: 
                word = ''
                break
    # If word is in dictionary and not already in words, append it to words 
        if word in dictionary and word not in words: 
            words.append(word)
            word = ''
        else: word = ''
    return words

# return a tuple of the highest-scoring word in the dictionary and its score
def findHighestWord(words, letterScores):
    highestWord = []
    score = 0
    for i in words:
        sum = 0 
        for j in i:

            # Use ord to figure out index
            index = ord(j) - ord('a')
            sum += letterScores[index]
        
        # If only one word, list has only one item
        if sum > score:
            highestWord = [i]
            score = sum
        
        # If more than one word with equal score, add items to list 
        elif sum == score: 
            highestWord.append(i)
    
    # return list
    return highestWord, score


def noSpacesInString(s):
    for c in s:
        if c.isspace():
            s = s.replace(c,'')
    return s
#################################################
# Problems
#################################################

# Fixed function
def buggyCleanUpCode(code):
    lines = code.splitlines()
    
    # Initialize necessary lists
    ansList = []
    
    # Get rid of blanks lines correctly
    noWhites = ridBlankLines(lines)    
   # Get rid of comments correctly
    for i in noWhites:
        if not '#' in i: ansList.append(i)
        else:
            # check if hash is inside quotation marks
            if (i.find('"') < i.find('#') and i.find('#') < i.rfind('"')):
                    ansList.append(i[:i.rindex('"')+1])
            elif (i.find("'") < i.find('#') and i.find('#') < i.rfind("'")):
                    ansList.append(i[:i.rindex("'")+1])
            elif i.index('#') > 0:
                ansList.append(i[:i.index('#')])
   
    # Get rid of spaces and join  
    return '\n'.join(ridBlankLines(ansList))

def bestScrabbleScore(dictionary, letterScores, hand):
    # Make list of words that can be made with hand
    words = makeWords(hand, dictionary)
  
    # Find words with highest score and highest score
    highestWords, score = findHighestWord(words, letterScores)

    # Return appropriate result based on length of highestWords list
    if len(highestWords) == 0:
        return None
    elif len(highestWords) == 1:
        return highestWords[0], score
    else: return highestWords, score

###### Autograded Bonus ########
# (place non-autograded bonus below #ignore-rest line!) #

def runSimpleProgram(program, args):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

# Print progam input on the left side of the screen
def drawInput(canvas, program):
    for i in range(len(program.splitlines())):
        canvas.create_text(10, i*17, text=program.splitlines()[i],
                           fill='grey', font="Helvetica 10")

# iterate over input and check starting string 
def tortoiseDraw(canvas, newProgram, color, x0, y0, angle):
    for i in newProgram.splitlines():
        # change color
        if i[0] == 'c':
            i = noSpacesInString(i)       
            color = i[i.index('r')+1:]
            if 'none' in color:
                color = ''
        # draw line 
        elif i[0] == 'm':
            n = int(i[i.index(' ')+1:])
            canvas.create_line(x0, y0, x0 + n*math.cos(angle), 
                    y0 + -1*(n*math.sin(angle)), fill=color, width=4)
            x0, y0 = x0 + n*math.cos(angle), y0 + -1*(n*math.sin(angle))
        # rotate left
        elif i[0] == 'l':
            i = noSpacesInString(i)
            degrees = i[i.index('t')+1:]
            angle += (int(degrees) * (math.pi / 180))
        # rotate right
        elif i[0] == 'r':
            i = noSpacesInString(i)
            degrees = i[i.index('t')+1:]
            angle -= (int(degrees) * (math.pi / 180)) 

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    
    # Print progam input on the left side of the screen 
    drawInput(canvas, program)

    # Get rid of comments and empty lines 
    newProgram = buggyCleanUpCode(program)
    color = ''
    x0, y0 = winWidth/2, winHeight/2
    angle = 0
    # iterate over input and check starting string 
    tortoiseDraw(canvas, newProgram, color, x0, y0, angle)
    root.mainloop()

def testRunSimpleTortoiseProgram1():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

def testRunSimpleTortoiseProgram2():
    runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

#################################################
# Test Functions
#################################################

def testBuggyCleanUpCode():
    print("Testing bestScrabbleScore()...", end="")
    code1 = \
    """def sample():
    x = "this is a cool string #this symbol can stay here"
    #this line should be removed
    print(s)
    
    """
    answer1 = 'def sample():\n    x = "this is a cool string #this symbol can '
    answer1Part2 = 'stay here"\n    print(s)'

    code2 = """
    # no comment
    def testsomething:
    code code code 

    if something then something else

    """

    answer2 = '    def testsomething:\n    code code code \n    if '
    answer2Part2 = 'something then something else'
    

    code3 = '\n\n\n\n\n#skldjd\ncode'
    answer3 = 'code'
    

    code4 = '\n\n\n'
    answer4 = ''

    code5= \
    """alksdjf
    #nocomment
    string = '###hashesinsidestring' #hashoutside
    #sldfjksjdf

    
    string = '\\n newline inside string'
    """
    answer5Part1 = "alksdjf\n    string = '###hashesinsidestring'\n    string"
    answer5Part2 = " = '\\n newline inside string'"

    assert(buggyCleanUpCode(code1) == answer1+answer1Part2)
    assert(buggyCleanUpCode(code2) == answer2+answer2Part2)
    assert(buggyCleanUpCode(code3) == answer3)
    assert(buggyCleanUpCode(code4) == answer4)
    assert(buggyCleanUpCode(code5) == answer5Part1+answer5Part2)
    print('passed')

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testBestScrabbleScore()
    testRunSimpleTortoiseProgram()
    testRunSimpleProgram()

def main():
    cs112_f17_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
