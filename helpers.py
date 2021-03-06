import pygame as pg
from piece import *

def initialize_positions(screen):
	""" Returns 2d array with either None values or piece objects"""
	letters = ["A","B","C","D","E","F","G","H"]
	sc = ["A", "H", "B", "G", "C", "F"]
	side_pieces = ["Rook", "Knight", "Bishop"]
	colour=None
	p_type=None
	out = []
	for number in range(1,9):
		row = []
		for letter in letters:
			# set pawns
			p = None
			if number==2:
				p = Pawn("White")
			if number==7:
				p = Pawn("Black")
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
					p = Queen("White")
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
					p = Queen("Black")
				if letter=="E":
					colour = "Black"
					p_type = "King"
			row.append(p)
		out.append(row)
	return out