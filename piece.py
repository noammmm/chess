import pygame as pg

class Piece:
	"""This is the class for a chess piece"""
	def __init__(self, pos, piece_type, colour, screen):
		self.x = pos[0]
		self.y = pos[1]
		self.piece_type = piece_type
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
	def __init__(self, pos, piece_type, colour, screen):
		super().__init__(pos, piece_type, colour, screen) 
	
	def logic():
		pass

class Rook(Piece):
	def __init__(self, pos, piece_type, colour):
		super().__init__(pos, piece_type, colour)
	def logic():
		pass

class Knight(Piece):
	def __init__(self, pos, piece_type, colour):
		super().__init__(pos, piece_type, colour)
	def logic():
		pass

class Bishop(Piece):
	def __init__(self, pos, piece_type, colour):
		super().__init__(pos, piece_type, colour)
	def logic():
		pass

class Queen(Piece):
	def __init__(self, pos, piece_type, colour):
		super().__init__(pos, piece_type, colour)
	def logic():
		pass

class King(Piece):
	def __init__(self, pos, piece_type, colour):
		super().__init__(pos, piece_type, colour)
	def logic():
		pass
