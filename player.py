from piece import *

class Player():

	def __init__(self, name, colour, ppos):
		
		self.name = name
		self.colour = colour
		self.ppos = ppos
		self.check = False
		self.checkMate = False

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
		for p in self.ppos[self.frontrow]:
			print(self.ppos[self.frontrow][p])
		for p in self.ppos[self.backrow]:
			print(self.ppos[self.backrow][p])


	def turn():
		pass

