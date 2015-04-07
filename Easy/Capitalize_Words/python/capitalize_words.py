import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			print " ".join([word[0].upper()+word[1:] for word in line.strip().split()])


if len(sys.argv) != 2:
	print "Usage ./capitalize_words.py <filename>"
	sys.exit(1)
main(sys.argv[1])