import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			print int(line.strip(), 16)

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])