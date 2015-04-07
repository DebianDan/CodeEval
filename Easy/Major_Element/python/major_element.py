import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			nums = [int(x) for x in line.strip().split(",")]
			for num in set(nums):
				if nums.count(num) > len(nums)/2:
					print num
					break
			else:
				print None

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])