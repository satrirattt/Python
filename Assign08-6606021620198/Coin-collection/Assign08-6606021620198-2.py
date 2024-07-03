#Workshop 2 : Coin Collection
import pgzrun
from random import randint

def place_coins():
    global coins
    coins = []
    for _ in range(3):
        while True:
            new_coin = Actor('coin')
            new_coin.x = randint(new_coin.width, WIDTH - new_coin.width)
            new_coin.y = randint(new_coin.height, HEIGHT - new_coin.height)
            coin_overlap = False
            for coin in coins:
                if new_coin.colliderect(coin):
                    coin_overlap = True
                    break
            if not coin_overlap:
                coins.append(new_coin)
                break

def draw():
    if Game_Over:
        screen.fill('black')
        screen.draw.text(f'Time out! Your score: {Score}', (200, 300), fontsize=50)
        screen.draw.text(f'Please Enter to play again', (200, 350), fontsize=50)
    else:
        screen.fill((100, 200, 100))
        screen.draw.text(f'Score: {Score}', (5, 10), fontsize=30)
        screen.draw.text(f'Time: {Time}', (690, 10), fontsize=30)
        fox.draw()
        for coin in coins:
            coin.draw()

def on_key_down(key, mod, unicode):
    global Score, Time, Game_Over
    if Game_Over:
        if key == keys.RETURN:
            Score = 0
            Time = 0
            Game_Over = False
            place_coins()
            fox.pos = (WIDTH/2, HEIGHT/2)
            clock.schedule_interval(count_time, 1.0)

def update():
    global Score
    if not Game_Over:
        if keyboard.left:
            if fox.left > 0:
                fox.x -= 2
        elif keyboard.right:
            if fox.right < WIDTH:
                fox.x += 2
        if keyboard.up:
            if fox.top > 0:
                fox.y -= 2
        elif keyboard.down:
            if fox.bottom < HEIGHT:
                fox.y += 2

    for coin in coins:
        if fox.colliderect(coin):
            sounds.ping.play()
            Score += 1
            coins.remove(coin)
            new_coin = Actor('coin')
            new_coin.x = randint(new_coin.width, WIDTH - new_coin.width)
            new_coin.y = randint(new_coin.height, HEIGHT - new_coin.height)
            coins.append(new_coin)

    if not coins:
        place_coins()

def count_time():
    global Time, Game_Over
    Time += 1
    if Time == MAX_TIME:
        Game_Over = True
        clock.unschedule(count_time)

TITLE = 'Coin Collection Game'
WIDTH, HEIGHT = 800, 600
Score = 0
Time = 0
Game_Over = False
MAX_TIME = 30
fox = Actor('fox', (WIDTH/2, HEIGHT/2))
place_coins()
clock.schedule_interval(count_time, 1.0)
pgzrun.go()

        
