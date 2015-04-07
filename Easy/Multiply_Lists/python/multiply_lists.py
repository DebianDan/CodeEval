import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			list1, list2 = [map(int, l.split()) for l in line.strip().split("|")]
			print ' '.join([str(x*y) for x,y in zip(list1, list2)])


if len(sys.argv) != 2:
	print "Usage ./multiply_lists.py <filename>"
	sys.exit(1)
main(sys.argv[1])