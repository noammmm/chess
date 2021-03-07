from piece import *

def initialize_positions():
	""" Returns 2d array with either None values or piece objects"""
	letters = ["A","B","C","D","E","F","G","H"]
	out = []
	# for number in range(1,9):
	codes = []
	for letter in letters:
		row = []
		# for letter in letters:
		for number in range(1,9):
			# set pawns
			c=letter+str(number)
			p = None
			if number==2:
				p = Pawn("White", [letter, number])
			if number==7:
				p = Pawn("Black", [letter, number])
			# back pieces			
			if number==1:
				# white back
				if letter=="F" or letter =="C":
					# make bishops
					p = Bishop("White", [letter, number])
				if letter=="B" or letter =="G":
					# make knights
					p = Knight("White", [letter, number])
				if letter=="A" or letter =="H":
					# make rooks
					p = Rook("White", [letter, number])
				if letter=="D":
					p = Queen("White", [letter, number])
				if letter=="E":
					p = King("White", [letter, number])

			if number==8:
				# black back
				if letter=="F" or letter =="C":
					# make bishops
					p = Bishop("Black", [letter, number])
				if letter=="B" or letter =="G":
					# make knights
					p = Knight("Black", [letter, number])
				if letter=="A" or letter =="H":
					# make rooks
					p = Rook("Black", [letter, number])
				if letter=="D":
					p = Queen("Black", [letter, number])
				if letter=="E":
					p = King("Black", [letter, number])
			row.append(p)
			codes.append(c)
		out.append(row)
	print(codes)
	return out