class Piece:
	"""This is the class for a chess piece"""
	def __init__(self, pos, piece_type, colour):
		self.x = pos[0]
		self.y = pos[1]
		self.piece_type = piece_type
		self.colour = colour

	def draw():
		pass

	def move():
		pass



class Pawn(Piece):
	pass
