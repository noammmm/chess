import pygame as pg
import sys
pg.init()
size = 200, 200
screen = pg.display.set_mode(size)
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()