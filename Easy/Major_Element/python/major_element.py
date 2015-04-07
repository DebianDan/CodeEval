import sys
from collections import defaultdict

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			nums = [int(x) for x in line.strip().split(",")]
			count_dict = defaultdict(int)
			for i in nums:
				count_dict[i] += 1
				if count_dict[i] > len(nums)/2:
					print i
					break
			else:
				print None

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])