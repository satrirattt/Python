#Example 11-5 : character animate
import pgzrun
def draw():
    screen.fill('white')
    if Index == 0: boy1.draw()
    elif Index == 1: boy2.draw()
    elif Index == 2: boy3.draw()
    elif Index == 3: boy4.draw()
    boy.draw()

def count_index():
    global Index
    Index = (Index + 1) % 4
    boy.image = image_name[Index]

WIDTH,HEIGHT,TITLE, = 640 ,480,'Test Character Animation3 '
Index = 0
image_name = ['boy_1','boy_2','boy_3','boy_4']
boy = Actor('boy_1',(WIDTH/2,HEIGHT/2))
boy1 = Actor('boy_1')
boy2 = Actor('boy_2')
boy3 = Actor('boy_3')
boy4 = Actor('boy_4')
clock.schedule_interval(count_index,0.10)
pgzrun.go()
        
        
        
