import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			# More readable version
			# sets = line.strip().split(";")
			# set1 = {int(i) for i in sets[0].split(",")}
			# set2 = {int(i) for i in sets[1].split(",")}
			set1, set2 = [set(map(int, s.split(","))) for s in line.strip().split(";")]
			print ",".join(map(str, sorted(set1 & set2)))

if len(sys.argv) != 2:
	print "Usage ./set_intersection.py <filename>"
	sys.exit(1)
main(sys.argv[1])