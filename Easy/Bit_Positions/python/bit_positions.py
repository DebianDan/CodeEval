import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			n, p1, p2 = [int(x) for x in line.strip().split(",")]
			b = bin(n)
			print str(b[-p1] == b[-p2]).lower()  #least significant bit is on the right

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])