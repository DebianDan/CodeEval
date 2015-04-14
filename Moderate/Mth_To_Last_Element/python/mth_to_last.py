import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			items = line.strip().split()
			index = int(items[-1])
			if index <= len(items):
				print items[-1 - index]

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])