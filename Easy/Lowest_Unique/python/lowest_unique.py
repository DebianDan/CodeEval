import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			game = [int(x) for x in line.strip().split()]
			num, count = 0, 0
			for i in sorted(game):
				if i != num and count == 1:
					print game.index(num)+1 #plus 1 since players are 1 indexed
					break
				elif i != num:
					num = i
					count = 1
				else:
					count += 1
			else:
				print 0

if len(sys.argv) != 2:
	print "Usage ./lowest_unique.py <filename>"
	sys.exit(1)
main(sys.argv[1])