import sys
from datetime import datetime

PATTERN = "%H:%M:%S"

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			d1, d2 = sorted(line.strip().split(), reverse=1) #always put the larger time in d1
			td = datetime.strptime(d1, PATTERN)  - datetime.strptime(d2, PATTERN)
			print str(td).rjust(8,'0')

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])