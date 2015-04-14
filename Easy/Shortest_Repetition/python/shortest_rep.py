import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			line = line.strip()
			for i in range(1, len(line)+1):
				sub = line[:i]
				if len([x for x in line.split(sub) if x]) == 0:
					print len(sub)
					break

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])