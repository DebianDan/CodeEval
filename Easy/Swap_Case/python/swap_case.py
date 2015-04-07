import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			print line.strip().swapcase()


if len(sys.argv) != 2:
	print "Usage ./swap_case.py <filename>"
	sys.exit(1)
main(sys.argv[1])