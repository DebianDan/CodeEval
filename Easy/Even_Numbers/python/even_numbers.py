import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			if int(line.strip()) % 2 == 0:
				print 1
			else:
				print 0
			
if len(sys.argv) != 2:
	print "Usage ./even_numbers.py <filename>"
	sys.exit(1)
main(sys.argv[1])