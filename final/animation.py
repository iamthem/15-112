from tkinter import * 
import math 

def init(data):
    data.planets = [] 
    

def timerFired(data):
    dtheta = math.pi / 100000
    for planet in data.planets:
        planet[0] += -1*planet[2]*math.sin(dtheta)
        planet[1] += 1*planet[2]*math.cos(dtheta)


def keyPressed(event, data):
    pass

def drawPlanets(data, canvas):
    if data.planets:
        for planet in data.planets:
            canvas.create_oval(planet[0] - 5, planet[1] - 5, planet[0] + 5, planet[1]+5,
                fill = 'blue')

def mousePressed(event, data):
    if ((event.x < data.width//2 - 50 or event.x > data.width//2 + 50 ) 
        and ( event.y < data.height//2 - 50 or 
        event.y > data.height//2 + 50)):
            r = math.sqrt((abs(event.y - data.height//2))**2 + 
                 (abs(event.x - data.width//2))**2)
            data.planets.append([event.x, event.y, r])

def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                    fill = 'black')
    canvas.create_oval(data.width//2 - 50, data.height//2 - 50, 
            data.width//2 + 50, data.height//2 + 50, fill = 'yellow')
    canvas.create_text(data.width//2, data.height//2, text=':)', fill = 'black')
    drawPlanets(data, canvas)


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

run(300, 300)
