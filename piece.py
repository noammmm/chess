import pygame as pg

class Piece:
	"""This is the class for a chess piece"""
	def __init__(self, colour, board_pos):
		self.colour = colour
		self.alive = True
		self.font = pg.font.SysFont(None, 18)
		self.pad = 40
		self.selected = False
		self.board_pos = board_pos
		# self.font = pg.font.SysFont(None, 28)
		# self.screen = screen
		if self.colour=="White":
			self.col = (225, 255, 255)
		else:
			self.col = (0,0,0)


	def draw(self, place, screen):
		img = self.font.render(self.piece_type, True, self.col)
		pg.draw.circle(screen, self.col, place[::-1], 4)
		screen.blit(img, place[::-1])
		if self.selected:
			pg.draw.circle(screen, (200, 200, 200), place[::-1], 25, width=2)

	def moveTo(self, position):
		pass



class Pawn(Piece):
	def __init__(self, colour, board_pos):
		super().__init__(colour, board_pos) 
		self.piece_type=" Pawn "
	
	def logic():
		pass

class Rook(Piece):
	def __init__(self, colour, board_pos):
		super().__init__(colour, board_pos)
		self.piece_type  = " Rook "
	def logic():
		pass

class Knight(Piece):
	def __init__(self, colour, board_pos):
		super().__init__(colour, board_pos)
		self.piece_type = "Knight"
	def logic():
		pass

class Bishop(Piece):
	def __init__(self, colour, board_pos):
		super().__init__(colour, board_pos)
		self.piece_type = "Bishop"
	def logic():
		pass

class Queen(Piece):
	def __init__(self, colour, board_pos):
		super().__init__(colour, board_pos)
		self.piece_type = "Queen "
	def logic():
		pass

class King(Piece):
	def __init__(self, colour, board_pos):
		super().__init__(colour, board_pos)
		self.piece_type = " King "
	def logic():
		pass
