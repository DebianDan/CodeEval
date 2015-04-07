import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			if line.strip() == "":
				continue
			print " ".join(reversed(line.split()))


if len(sys.argv) != 2:
	print "Usage ./reverse_words.py <filename>"
	sys.exit(1)
main(sys.argv[1])