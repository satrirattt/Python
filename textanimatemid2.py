import pgzrun

def draw():
    screen.fill( BGColor )
    screen.draw.text("Show Text Animate", (250,10),fontsize=28,color='blue')
    screen.draw.text("Python", (x1,120),fontsize=30,color='red')
    screen.draw.text("Pygame Zero", (x2,360),fontsize=40,color='red')

def update():
    global x1,x2
    x1 = x1 + 2
    if x1 > WIDTH: x1 = 0
    x2 = x2 - 1
    if x2 < 0: x2 = WIDTH

TITLE = 'Text Animate'
WIDTH = 640
HEIGHT = 480
BGColor = (255,255,255)
x1 = int(WIDTH/2)
x2 = int(WIDTH/2)

pgzrun.go()
