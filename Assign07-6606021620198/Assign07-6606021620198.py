import pgzrun

WIDTH = 1024
HEIGHT = 768

image_filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
sound = sounds.load("woosh.wav")
current_image = 0

def change_image():
    global current_image
    current_image = (current_image + 1) % len(image_filenames)
    sounds.woosh.play()

def draw():
    screen.clear()
    screen.blit(image_filenames[current_image], (230,0))

def on_mouse_down(pos):
    change_image()

def on_key_down(key):
    change_image()
pgzrun.go()
