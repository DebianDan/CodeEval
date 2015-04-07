import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			words = line.strip().split(";")
			nums = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
			result = ""
			for word in words:
				result += str(nums[word])
			print result
			

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])