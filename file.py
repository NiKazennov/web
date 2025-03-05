from pygame import *


init()
# Код, описывающий окно программы
width = 400  
height = 400  
screen = display.set_mode([width, height])

# Создаём контроль FPS
clock = time.Clock()  
FPS = 2  

y=100
x=100
w1=200
h1=200


# Игровой цикл и флаг выполнения программы
game_run = True
while game_run:
    for i in event.get():
        if i.type == QUIT:  
            game_run = False

    # БЛОК ИГРОВОЙ ЛОГИКИ
    if x > 150 or y > 150:
        x=100
        y=100
        y=100
    if w1 < 100 or h1 < 100:
        w1=200
        h1=200

    # БЛОК ОТРИСОВКИ ОБЪЕКТОВ В ОКНЕ ПРОГРАММЫ
    x=x+50
    y=y+50
    w1=w1-100
    h1=h1-100
    screen.fill([255,255,255])
    draw.rect(screen,[255,0,0],[x,y,w1,h1])


    # Отображение нарисованных объектов
    display.flip()

    # Контроль FPS
    clock.tick(FPS)

quit()