#Example 11-2 : use clock
import pgzrun
def draw():
    screen.fill((255,255,255))
    screen.draw.text(f'Time 1 : {time1}',(10,10),color='blue')
    screen.draw.text(f'Time 2 : {time1}',topright=(WIDTH-10,10),color='magenta')

def on_mouse_down(pos,button):
    clock.schedule(count_time_1,1.0)

def count_time_1():
    global time1
    time1 +=1

def count_time_2():
    global time2
    time2 +=1
    if time2 == 20:
        clock.unschedule(count_time_2)
        print('stop clock')

WIDTH,HEIGHT,TITLE, = 400 ,300,'Test Clock'  
time1 = time2 =0
clock.schedule(count_time_1,5.0)#call once time
clock.schedule_interval(count_time_2,1.0)#call loop
pgzrun.go()
        
        
        
