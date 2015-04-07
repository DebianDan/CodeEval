import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			n, m = [int(i) for i in line.split(",")]
			if m>n:
				print n
			else:
				print n-(m*(n/m))
			
if len(sys.argv) != 2:
	print "Usage ./n_mod_m.py <filename>"
	sys.exit(1)
main(sys.argv[1])