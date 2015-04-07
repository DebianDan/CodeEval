import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			if line.strip() == "":
				continue
			S, c = line.strip().split(",")
			print S.rfind(c)


if len(sys.argv) != 2:
	print "Usage ./rightmost_char.py <filename>"
	sys.exit(1)
main(sys.argv[1])