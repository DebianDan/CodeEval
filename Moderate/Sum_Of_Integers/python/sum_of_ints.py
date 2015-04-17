import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			nums = map(int, line.strip().split(","))
			max_sum = nums[0]
			for i in xrange(1, len(nums)+1):
				for j in xrange(len(nums)+1-i):
					sliding_sum = sum(nums[j:j+i])
					if sliding_sum > max_sum:
						max_sum = sliding_sum
			print max_sum

if len(sys.argv) != 2:
	print "Usage ./max_range_sum.py <filename>"
	sys.exit(1)
main(sys.argv[1])