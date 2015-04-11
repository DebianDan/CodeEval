import sys
from collections import defaultdict

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			s = ''.join(c for c in line.lower() if c.isalpha())
			count_dict = defaultdict(int)
			for c in s:
				count_dict[c] += 1
			maxb, beauty = 0, 26
			for i in sorted(count_dict.values(), reverse=1):
				maxb += beauty*i
				beauty -= 1
			print maxb


if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])