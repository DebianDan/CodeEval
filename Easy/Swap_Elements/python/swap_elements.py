import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			nums, swaps = [l.strip() for l in line.split(":")]
			nums = nums.split()
			swaps = [[int(x) for x in pos.strip().split("-")] for pos in swaps.split(",")]
			for swap in swaps:
				nums[swap[0]], nums[swap[1]] = nums[swap[1]], nums[swap[0]]
			print " ".join(nums)

if len(sys.argv) != 2:
	print "Usage ./swap_elements.py <filename>"
	sys.exit(1)
main(sys.argv[1])