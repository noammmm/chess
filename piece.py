import pygame as pg
from chess import screen

class Piece:
	"""This is the class for a chess piece"""
	def __init__(self, colour):
		self.colour = colour
		self.alive = True
		self.font = pg.font.SysFont(None, 28)
		self.screen = screen


	def draw(self):

		img = self.font.render(self.piece_type, True, (255, 255, 255))
		self.screen.blit(img, (self.x, self.y))

	def moveTo(position):
		pass



class Pawn(Piece):
	def __init__(self, colour):
		super().__init__(colour) 
		self.piece_type="Pawn"
	
	def logic():
		pass

class Rook(Piece):
	def __init__(self, colour):
		super().__init__(colour)
		self.piece_type  = "Rook"
	def logic():
		pass

class Knight(Piece):
	def __init__(self, colour):
		super().__init__(colour)
		self.piece_type = "Knight"
	def logic():
		pass

class Bishop(Piece):
	def __init__(self, colour):
		super().__init__(colour)
		self.piece_type = "Bishop"
	def logic():
		pass

class Queen(Piece):
	def __init__(self, colour):
		super().__init__(colour)
		self.piece_type = "Queen"
	def logic():
		pass

class King(Piece):
	def __init__(self, colour):
		super().__init__(colour)
		self.piece_type = "King"
	def logic():
		pass
