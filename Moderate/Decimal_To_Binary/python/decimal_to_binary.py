import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			n = int(line.strip())
			print bin(n)[2:] #remove the 0b from the string


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])