import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			num,op = line.strip().split()
			if "-" in op:
				i = op.index("-")
				print int(num[:i]) - int(num[i:])
			else:
				i = op.index("+")
				print int(num[:i]) + int(num[i:])

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])