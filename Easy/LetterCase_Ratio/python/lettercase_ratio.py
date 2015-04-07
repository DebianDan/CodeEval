import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			lower, length = 0, float(len(line)-1)
			for c in line:
				if c.islower():
					lower += 1
			print 'lowercase: {0:.2f} uppercase: {1:.2f}'.format((lower/length)*100, ((length-lower)/length)*100)


if len(sys.argv) != 2:
	print "Usage ./lettercase_ratio.py <filename>"
	sys.exit(1)
main(sys.argv[1])