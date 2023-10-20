import pgzrun
import random

WIDTH = 800
HEIGHT = 600
BGColor = (0, 0, 0)

texts = ["Python", "Pygame Zero1", "Pygame Zero2", "Pygame Zero3", "Pygame Zero4"]
speeds = [random.randint(1, 4) for _ in range(len(texts))]
y_positions = [-100, -200, -300, -400, -500]

def draw():
    screen.clear()
    screen.draw.text("Show Text Animate", (250, 10), fontsize=28, color='blue')
    for i in range(len(texts)):
        screen.draw.text(texts[i], (30 + i * 100,y_positions[i]), fontsize=40, color='red')

def update():
    for i in range(len(texts)):
        y_positions[i] += speeds[i]
        if y_positions[i] > HEIGHT:
            y_positions[i] = -100

pgzrun.go()
