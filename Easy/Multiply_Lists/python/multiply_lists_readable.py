import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			lists = line.strip().split("|")
			list1, list2 = [map(int, l.split()) for l in lists]
			result = [str(x*y) for x,y in zip(list1, list2)]
			print ' '.join(result)


if len(sys.argv) != 2:
	print "Usage ./multiply_lists.py <filename>"
	sys.exit(1)
main(sys.argv[1])