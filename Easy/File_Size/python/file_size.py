import sys
import os

def main(filename):
	print os.stat(filename).st_size

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])