import pygame as pg
from piece import *

def initialize_positions():
	""" Returns 2d array with either None values or piece objects"""
	letters = ["A","B","C","D","E","F","G","H"]
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
				if letter=="F" or letter =="C":
					# make bishops
					p = Bishop("White")
				if letter=="B" or letter =="G":
					# make knights
					p = Knight("White")
				if letter=="A" or letter =="H":
					# make rooks
					p = Rook("White")
				if letter=="D":
					colour = "White"
					p_type = "Queen"
					p = Queen("White")
				if letter=="E":
					colour = "White"
					p_type = "King"
					p = King("White")

			if number==8:
				# black back
				if letter=="F" or letter =="C":
					# make bishops
					p = Bishop("Black")
				if letter=="B" or letter =="G":
					# make knights
					p = Knight("Black")
				if letter=="A" or letter =="H":
					# make rooks
					p = Rook("Black")
				if letter=="D":
					p = Queen("Black")
				if letter=="E":
					p = King("Black")
			row.append(p)
		out.append(row)
	return out