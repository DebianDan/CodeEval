import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			if len(line) > 55:
				line = line[:40].rsplit(" ", 1)[0] + "... <Read More>" #Split once on the last space
			print line

if len(sys.argv) != 2:
	print "Usage ./read_more.py <filename>"
	sys.exit(1)
main(sys.argv[1])