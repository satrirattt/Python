import pgzrun

def draw():
    screen.fill(('white'))
    screen.draw.text("Hello World" , topleft=(10,10),fontsize=30 , color = 'black')
    screen.draw.text("Hello World" , topright=(620,10),fontsize=30 , color = 'red')
    screen.draw.text("Hello World" , bottomleft=(10,450),fontsize=30 , color = 'green')
    screen.draw.text("Hello World" , bottomright=(620,450),fontsize=30 , color = 'blue')
    screen.draw.text("Hello World" , center=(320,240),fontsize=30 , color = 'magenta')

TITIE = "Display Text By Pygame Zero"
WIDTH = 640
HEIGHT = 480

pgzrun.go()
