import pygame as pg

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