import sys

def loopAll(filename):
	"""
	loop through the entire matrix for each case to determine the minimum number
	of consectutive . between a X and Y
	"""
	with open(filename, "r") as f:
		for line in f:
			deets, minY = line.strip().split(","), 10
			for d in deets:	
				counter = 0
				for c in d:
					if c == ".":
						counter +=1
					elif c == "Y":
						break
				if counter == 0:
					minY = 0
					break
				elif counter < minY:
					minY = counter
			print minY

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			# 2 <= N <= 10 means at most there will be 8 consectutive .
			for i in xrange(0,9):
				if line.find("X" + "."*i + "Y") != -1:
					print i
					break


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main2(sys.argv[1])