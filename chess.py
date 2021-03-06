import pygame as pg
import sys
from helpers import *
from piece import *
from player import *


def drawchequerboard(n, size):
	sqrsize = size[0]/n
	count = 0
	for x in range(n):
		for y in range(n):
			x_ = x*sqrsize
			y_ = y*sqrsize
			
			if count%2==0:
				col = (118, 150, 85)
			else:
				col = (40,40,40)
			pg.draw.rect(screen, col, 
						(x_, y_, sqrsize, sqrsize))
			count+=1
		count+=1


if __name__ == "__main__":

	player1 = Player("Alice", "White")
	player2 = Player("Bob", "Black")

	pg.init()

	green = (118, 150, 85)
	size = 400, 400
	screen = pg.display.set_mode(size)

	p = Pawn((1, 2),"King", "black")
	print(p.colour)

	print(initialize_positions())


	# Loop
	while 1:
	    for event in pg.event.get():
	        if event.type == pg.QUIT: sys.exit()
	    screen.fill(green)
	    drawchequerboard(8, size)

	    pg.display.update()