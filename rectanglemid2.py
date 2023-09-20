import pgzrun

def draw():
    screen.clear()
    screen.draw.rect(Rect((0,0),(200,150)),(255,255,255))
    screen.draw.rect(Rect((200,0),(200,150)),(0,255,0))
    screen.draw.rect(Rect((0,150),(200,150)),(0,255,0))
    screen.draw.rect(Rect((2000,150),(200,150)),(255,255,255))

    
    for n in range(5):
        screen.draw.rect(Rect((150+(n*10),100+(n*10)),(100,100)),'yellow')
    

TITIE = 'Test Rectangle by Pygame Zero'
WIDTH = 400
HEIGHT = 300

pgzrun.go()
