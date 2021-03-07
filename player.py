from piece import Rook, Knight, Bishop, Queen, King, Pawn

class Player():

	def __init__(self, name, colour, board):

		self.name = name
		self.colour = colour
		self.board = board
		self.check = False
		self.checkMate = False
		# self.screen = screen

		if self.colour=="White":
			self.frontrow = 1
			self.backrow = 0
			self.turn = True

		if self.colour=="Black":
			self.frontrow = 6
			self.backrow = 7
			self.Turn = False


		self.init_pieces()

	def init_pieces(self):
		pass


	def turn():
		pass

