import sys

def main(filename):
	with open(filename, 'r') as f:
		total = 0
		for line in f:
			total += int(line)
		print total

if len(sys.argv) != 2:
	print "Usage ./sum_of_ints.py <filename>"
	sys.exit(1)
main(sys.argv[1])