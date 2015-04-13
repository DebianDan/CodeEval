import sys

def slow(filename):
	"""
	runs in O(n^2), checks the min of each num from 1 to max(n.value)
	"""
	with open(filename, 'r') as f:
		for line in f:
			nums = map(int, line.strip().split())
			mini = 1000000
			for i in range(1,max(nums[1:])+1):
				dist = findMinDist(nums[1:], i)
				if dist < mini:
					mini = dist
			print mini

def findMinDist(nums, address):
	total = 0
	for n in nums:
		total += abs(address-n)
	return total

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			nums = map(int, line.strip().split())
			baseline = sum(nums[1:])/nums[0]
			nums = nums[1:]
			curr = findMinDist(nums, baseline)
			if findMinDist(nums, baseline+1) < curr:
				last = findMinDist(nums, baseline+1)
				for i in xrange(baseline+2,max(nums)):
					curr = findMinDist(nums, i)
					if curr > last:
						print last
						break
					last = curr
			elif findMinDist(nums, baseline-1) < curr:
				last = findMinDist(nums, baseline-1)
				for i in xrange(baseline-2,0,-1):
					curr = findMinDist(nums, i)
					if curr > last:
						print last
						break
					last = curr
			else:
				print curr
				continue

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])