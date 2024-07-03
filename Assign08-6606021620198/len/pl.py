import pgzrun

WIDTH = 800
HEIGHT = 600

text = "Bouncing Text"
text_x = WIDTH // 2
text_y = HEIGHT // 2
velocity_x = 5
velocity_y = 3

def update():
    global text_x, text_y, velocity_x, velocity_y

    # Move the text by adding the velocity to its position
    text_x += velocity_x
    text_y += velocity_y

    # Check for collision with the window borders
    if text_x < 0 or text_x + len(text) * 10 > WIDTH:
        velocity_x = -velocity_x  # Reverse the horizontal velocity

    if text_y < 0 or text_y > HEIGHT:
        velocity_y = -velocity_y  # Reverse the vertical velocity

def draw():
    screen.clear()
    screen.draw.text(text, (text_x, text_y), color="white", fontsize=40)

pgzrun.go()
