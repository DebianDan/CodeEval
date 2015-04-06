import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			print sum([int(x) for x in line.strip()])

if len(sys.argv) != 2:
	print "Usage ./sumdigits.py <filename>"
	sys.exit(1)
main(sys.argv[1])