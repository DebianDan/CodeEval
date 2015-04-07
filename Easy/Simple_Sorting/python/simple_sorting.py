import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			print " ".join("%0.3f" % i for i in sorted([float(num) for num in line.split()]))
			
if len(sys.argv) != 2:
	print "Usage ./simple_sorting.py <filename>"
	sys.exit(1)
main(sys.argv[1])