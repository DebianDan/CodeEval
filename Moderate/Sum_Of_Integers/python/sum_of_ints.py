import sys

def sliding_window_brute_force(nums):
	max_sum = nums[0]
	for i in xrange(1, len(nums)+1):
		for j in xrange(len(nums)+1-i):
			sliding_sum = sum(nums[j:j+i])
			if sliding_sum > max_sum:
				max_sum = sliding_sum
	return max_sum


# Implementing Traditional Kadane's algorithm to the Maximum subarray problem
# http://en.wikipedia.org/wiki/Maximum_subarray_problem
# Runs in O(n) linear time
def traditional_max_subarray(nums):
	max_ending_here = current_max = 0
	for num in nums:
	    max_ending_here = max(0, max_ending_here + num)
	    current_max = max(current_max, max_ending_here)
	return current_max

# Implementing Kadane's algorithm to the Maximum subarray problem
# http://en.wikipedia.org/wiki/Maximum_subarray_problem
# Runs in O(n) linear time
# The max could be negative, instead of allowing zero-len subarrays 
def max_subarray(nums):
	max_ending_here = current_max = nums[0]
	for num in nums[1:]:
	    max_ending_here = max(num, max_ending_here + num)
	    current_max = max(current_max, max_ending_here)
	return current_max

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			nums = map(int, line.strip().split(","))
			print max_subarray(nums)


if len(sys.argv) != 2:
	print "Usage ./max_range_sum.py <filename>"
	sys.exit(1)
main(sys.argv[1])