#Workshop 1 : Shoot the Fruits
import pgzrun
from random import randint

def draw():
    if Game_Over:
        screen.fill('black')
        screen.draw.text(f'Time out !, your score : {Score}',(200,300),fontsize=50)
        screen.draw.text(f'Please Click play again',(200,350),fontsize=50)
    else: 
        screen.fill((100,200,200))
        screen.draw.text(f'Score : {Score}',(690,10),fontsize=30)
        screen.draw.text(f'Time : {Time}',(5,10),fontsize=30)
        apple.draw()
        orange.draw()
        pineapple.draw()
    

def place_apple():
    apple.x = randint(apple.width,WIDTH - apple.width)
    apple.y = 0
    apple.speed = randint(3,5)

def place_orange():
    orange.x = randint(orange.width,WIDTH - orange.width)
    orange.y = 0
    orange.speed = randint(3,5)

def place_pineapple():
    pineapple.x = randint(pineapple.width,WIDTH - pineapple.width)
    pineapple.y = 0
    pineapple.speed = randint(3,5)
    
def on_mouse_down(pos,button):
    global Score,Time,Game_Over
    if button == mouse.LEFT and apple.collidepoint(pos):
        sounds.ping.play()
        Score += 1
        place_apple()
    if button == mouse.LEFT and orange.collidepoint(pos):
        sounds.ping.play()
        Score += 1
        place_orange()
    if button == mouse.LEFT and  pineapple.collidepoint(pos):
        sounds.ping.play()
        Score += 1
        place_pineapple()

    if Game_Over:
        if button == mouse.LEFT:
            Score = 0
            Time = 0
            Game_Over = False
            place_apple()
            place_orange()
            place_pineapple()
            clock.schedule_interval(count_time,1.0)

def update():
    apple.y += apple.speed
    if (apple.y > HEIGHT):
        place_apple()
    orange.y += orange.speed
    if (orange.y > HEIGHT):
        place_orange()
    pineapple.y += pineapple.speed
    if (pineapple.y > HEIGHT):
        place_pineapple()

def count_time():
    global Time,Game_Over
    Time += 1
    if Time == MAX_TIME:
        Game_Over = True
        clock.unschedule(count_time)

WIDTH = 800
HEIGHT = 600
TITLE = "Shoot the fruits"
Score = 0
Time = 0
Game_Over = False
MAX_TIME = 60
apple = Actor('apple')
place_apple()
orange = Actor('orange')
place_orange()
pineapple = Actor('pineapple')
place_pineapple()
clock.schedule_interval(count_time,1.0)
pgzrun.go()
