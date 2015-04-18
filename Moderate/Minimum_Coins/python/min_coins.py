import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			n = int(line.strip())
			coins = 0
			for i in [5,3,1]:
				if n >= i:
					num = n/i
					coins += num
					n -= i*num
			print coins 



if len(sys.argv) != 2:
	print "Usage ./max_range_sum.py <filename>"
	sys.exit(1)
main(sys.argv[1])