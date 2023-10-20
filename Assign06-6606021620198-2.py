import pgzrun
import random

WIDTH = 800
HEIGHT = 600
BGColor = (0, 0, 0)

num_circles = random.randint(1, 8)

circles = []
for _ in range(num_circles):
    circle = {
        'x': random.randint(0, WIDTH),
        'y': random.randint(0, HEIGHT),
        'radius': random.randint(20, 50),
        'speed': random.uniform(1, 5)
    }
    circles.append(circle)

def draw():
    screen.clear()
    for circle in circles:
        screen.draw.circle((circle['x'], circle['y']), circle['radius'], 'white')

def update():
    for circle in circles:
        circle['x'] += circle['speed']
        if circle['x'] > WIDTH:
            circle['x'] = 0

pgzrun.go()
