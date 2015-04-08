import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			result = []
			for i in line.strip().split(","):
				if i not in result:
					result.append(i)
			print ",".join(result)

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])