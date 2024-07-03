import pgzrun
def draw():
    screen.fill((255,255,255))
    screen.draw.rect(Rect((400,250),(50,50)),'blue')
    ufo.draw()
    ufo1.draw()

def on_mouse_down(pos,button):
    if button == mouse.LEFT and ufo.collidepoint(pos):
        print('shoot ufo')
    elif button == mouse.LEFT and ufo.collidepoint(pos):
        print('shoot ufo1')
    if button == mouse.LEFT:
        print('no shoot')

def update():
    if keyboard.LEFT:
        ufo.x -= 2
    elif keyboard.RIGHT:
        ufo.x += 2
    elif keyboard.UP:
        ufo.y -= 2
    elif keyboard.DOWN:
        ufo.y += 2
    if ufo.colliderect(ufo1):
        print('collision ufo')
    if ufo.colliderect(Rect((400,250),(50,50))):
        print('collision Rect')

TITLE,WIDTH,HEIGHT = 'Test Collision' , 500 ,300
ufo = Actor('ufo')
ufo1 = Actor('ufo',(WIDTH/2,HEIGHT/2))
pgzrun.go()
        
        
        
