import pygame as pg

pg.init()

CAPTION = "TOP FIRST BLOOD"
ICON = pg.image.load("mine.png")
WIDTH = 640
HEIGHT = 360
FPS = 60

WINDOW = pg.display
WINDOW.set_caption(CAPTION)
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode((WIDTH,HEIGHT))

RUNNING = True

RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = ( 0, 255, 0)

while RUNNING:
    pg.time.Clock().tick(FPS)

    SCREEN.fill((0,0,0))
    pg.draw.rect(SCREEN, RED, [30 , 30, 200, 10])#왼쪽, 위, 크기
    pg.draw.rect(SCREEN, RED, [80 , 30, 10, 100])
    pg.draw.rect(SCREEN, RED, [180 , 30, 10, 100])
    pg.draw.rect(SCREEN, RED, [30 , 130, 200, 10])
    pg.draw.rect(SCREEN, RED, [250 , 10, 10, 300])
    pg.draw.rect(SCREEN, RED, [250 , 10, 10, 300])
    


    pg.display.update()

    for event in pg.event.get():
            if event.type == pg.QUIT:
                    pg.display.quit()
                    RUNNING = False
