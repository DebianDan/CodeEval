import sys

class Board(object):
	def __init__(self):
		self.board = [[0 for j in range(256)] for i in range(256)]

	def setRow(self, i, x):
		self.board[i] = [x]*256

	def setCol(self, j, x):
		for i in range(256):
			self.board[i][j] = x

	def queryRow(self, i):
		return sum(self.board[i])

	def queryCol(self, j):
		total = 0
		for i in range(256):
			total += self.board[i][j]
		return total

def main(filename):
	m = Board()
	with open(filename, 'r') as f:
		for line in f:
			args = line.strip().split()
			if args[0] == "SetCol":
				m.setCol(int(args[1]), int(args[2]))
			elif args[0] == "SetRow":
				m.setRow(int(args[1]), int(args[2]))
			elif args[0] == "QueryCol":
				print m.queryCol(int(args[1]))
			elif args[0] == "QueryRow":
				print m.queryRow(int(args[1]))


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])