class Piece:
	"""This is the class for a chess piece"""
	def __init__(self, pos, piece_type, colour):
		self.x = pos[0]
		self.y = pos[1]
		self.piece_type = piece_type
		self.colour = colour
		self.alive = True

	def draw():
		pass

	def moveTo(position):
		pass



class Pawn(Piece):
	def __init__(self, pos, piece_type, colour):
		super().__init__(pos, piece_type, colour) 
	
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
