import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			items = line.strip().split(",")
			nums, words = [], []
			for item in items:
				if item.isalpha():
					words.append(item)
				else:
					nums.append(item)
			if len(words) == 0 or len(nums) == 0:
				print line.strip()
			else:
				print ",".join(words) + "|" + ",".join(nums)

if len(sys.argv) != 2:
	print "Usage ./mixed_content.py <filename>"
	sys.exit(1)
main(sys.argv[1])