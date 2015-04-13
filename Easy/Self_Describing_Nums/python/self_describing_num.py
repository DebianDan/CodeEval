import sys
from collections import defaultdict

def dictionary_sol(filename):
	"""
	Builds a dictionary of counts instead of fetching .count every time
	"""
	with open(filename, "r") as f:
		for line in f:
			num = line.strip()
			count_dict = defaultdict(int)
			for i in num:
				count_dict[int(i)] += 1
			for i in xrange(len(num)):
				if num[i] != str(count_dict[i]):
					print 0
					break
			else:
				print 1

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			num = line.strip()
			for i in xrange(len(num)):
				if num[i] != str(num.count(str(i))):
					print 0
					break
			else:
				print 1

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])