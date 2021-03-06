import pygame as pg
import sys
from helpers import *
from piece import *

pg.init()

green = (118, 150, 85)
size = 400, 400
screen = pg.display.set_mode(size)

p = Pawn((1, 2),"King", "black")
print(p.colour)



def initialize_positions():
	letters = ["A","B","C","D","E","F","G","H"]
	sc = ["A", "H", "B", "G", "C", "F"]
	side_pieces = ["Rook", "Knight", "Bishop", "Queen"]
	colour=None
	p_type=None
	squares = []
	for number in range(1,9):
		for letter in letters:
			# set pawns
			colour = None
			p_type = None
			if number==2:
				colour = "White"
				p_type = "Pawn"
			if number==7:
				colour = "Black"
				p_type = "Pawn"
			# back pieces			
			if number==1:
				# white back
				for i in range(0, len(sc), 2):
					if letter == sc[i] or letter == sc[i+1]:
						colour = "White"
						p_type = side_pieces[i//2]
				if letter=="D":
					colour = "White"
					p_type = "Queen"
				if letter=="E":
					colour = "White"
					p_type = "King"

			if number==8:
				# black back
				for i in range(0, len(sc), 2):
					if letter == sc[i] or letter == sc[i+1]:
						colour = "Black"
						p_type = side_pieces[i//2]	
				if letter=="D":
					colour = "Black"
					p_type = "Queen"
				if letter=="E":
					colour = "Black"
					p_type = "King"

			squares.append({letter:number, "piece":(colour, p_type)})
	return squares

print(initialize_positions())


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
	while 1:
	    for event in pg.event.get():
	        if event.type == pg.QUIT: sys.exit()
	    screen.fill(green)
	    drawchequerboard(8, size)

	    pg.display.update()