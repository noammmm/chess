import pygame as pg
import sys, copy
from helpers import *
from piece import *
from player import *


size = wwidth, wheight =  480, 480
screen = pg.display.set_mode(size)

def drawchequerboard(n, size):
	lttr = ["A","B","C","D","E","F","G","H"]
	sqrsize = 50 # size[0]/n 
	pad = 40
	count = 0
	# pg.draw.rect(screen, 
	# 			(80, 140, 60), 
	# 			(pad-5, pad-5, 410,410))

	for x in range(n):
		for y in range(n):
			x_ = x*sqrsize
			y_ = y*sqrsize
			
			if count%2==0:
				col = (130, 190, 100)
			else:
				col = (40,40,40)
			pg.draw.rect(screen, col, 
						(x_+pad, y_+pad, sqrsize, sqrsize))

			count+=1
		count+=1
	for y in range(n):
		# letters
		img = font.render(lttr[y], True, (255, 255, 255))
		screen.blit(img, (y*sqrsize + sqrsize*0.4 + pad,sqrsize*0.2))
		# numvers
		img = font.render(str(y+1), True, (255, 255, 255))
		screen.blit(img, (sqrsize*0.2, y*sqrsize + sqrsize*0.4 + pad))

def pprint(board_):
	b_ = [[0]*len(board_) for _ in range (len(board_))]
	for i in range(len(board_)):
		for j in range(len(board_)):
			if board_[i][j] is not None:
				b_[i][j]=board_[i][j].piece_type
			else:
				b_[i][j]='____'
		print(b_[i], "\n")


if __name__ == "__main__":

	pg.init()

	font = pg.font.SysFont(None, 18)

	green = (118, 150, 85)
	# print
	
	board = initialize_positions(screen)
	pprint(board)
	print(board)

	# p1 = Pawn((100, 100),"White", screen)
	# print(p1.piece_type)
	sys.exit()

	player1 = Player("Alice", "White", board, screen)
	# player2 = Player("Bob", "Black", initial_positions)
	# Main loop
	while 1:
	    for event in pg.event.get():
	        if event.type == pg.QUIT: sys.exit()
	    screen.fill(green)

	    drawchequerboard(8, size)

	    # p1.draw()
	    
	    # sys.exit()
	    pg.display.update()