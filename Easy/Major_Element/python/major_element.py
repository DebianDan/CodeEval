import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			nums = line.strip().split(",")
			major = len(nums)/2
			for i in xrange(major+1):
				num = nums[i]
				if nums.count(num) > major:
					print num
					break
			else:
				print None

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])