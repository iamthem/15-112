# Leandro Lopez

# lslopez

# Section H


#####################
# Hw 6
#####################
from tkinter import *
import random 
import math
import cs112_f17_week6_linter
####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.gameState = 'Start'
    data.xVelocity = 25
    data.yVelocity = 25
    data.radius = random.choice([5,15,25])
    data.x = random.randint(0,data.width-data.radius-1)
    data.y = random.randint(0, data.height-data.radius-1)
    data.xLocation = data.width//2 
    data.yLocation = data.height//2

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data, canvas):
    if data.gameState == 'Start':
        if (event.keysym == "p"): data.gameState = 'Game'
    elif data.gameState == 'Game':
        if (event.keysym == "Right"): movePlayer(canvas, 1, 'x') 
        if (event.keysym == "Left"): movePlayer(canvas, -1, 'x') 
        if (event.keysym == "Up"): movePlayer(canvas, -1, 'y')
        if (event.keysym == "Down"): movePlayer(canvas, 1, 'y') 

def movePlayer(canvas, n, direction):
    if direction == 'x':
        canvas.xview_scroll(n, 'units')
    elif direction == 'y':
        canvas.yview_scroll(n, 'units')

def timerFired(data):
    if data.gameState == 'Start':
        data.x += data.xVelocity
        data.y += data.yVelocity
        if data.x + data.radius >= data.width or data.x - data.radius <= 0:
            data.xVelocity *= -1

        if data.y + data.radius  >= data.height or data.y - data.radius <= 0:
            data.yVelocity *= -1

    elif data.gameState == 'Game':
        counter = 0 
        if counter % 5:
            data.xLocation = random.randint(-(1/3)*data.width, (2/3)*data.width) 
            data.yLocation = random.randint(-(1/3)*data.height, (2/3)*data.height)
        counter += 1

         
def drawStartScreen(canvas, data):
    canvas.create_text(data.width//2, data.height//4, fill="black",
            text='Targets Game!', font='Calibri 25 bold')
    
    canvas.create_text(data.width//2, data.height*3//4, fill="black",
            text="Press 'p' to play", font='Calibri 15 bold')

def drawCircle(canvas,x, y, r, color):
    canvas.create_oval(x-r,y-r, x+r, y+r, fill=color, width=0)

def drawMovingTarget(canvas, data):
    for i in range(5, 0, -1):
        if i % 2 == 0:
            drawCircle(canvas, data.x, data.y, (data.radius/5)*i, 'white')
        else:
            drawCircle(canvas, data.x, data.y, (data.radius/5)*i, 'red') 

def redrawAll(canvas, data):
    # draw in canvas
    if data.gameState == 'Start':
        drawStartScreen(canvas, data)
        drawMovingTarget(canvas, data)
    elif data.gameState == 'Game':
         canvas.create_rectangle(-1*data.xLocation, -1*data.yLocation, 
        2*data.width - data.xLocation, 2*data.height - data.yLocation, fill='white', width=5)
         drawRandomTarget(canvas, data)

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
        keyPressed(event, data, canvas)
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

run(400, 400)
