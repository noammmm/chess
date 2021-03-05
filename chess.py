import pygame as pg
import sys
pg.init()
green = (118, 150, 85)
size = 1000, 1000
screen = pg.display.set_mode(size)
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    screen.fill(green)
    pg.display.update()
    pg.draw.rect(screen, (255, 255, 255), (10, 10, 10 ,10 ))
    pg.display.update()

