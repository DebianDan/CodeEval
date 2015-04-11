import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			last, result = -1, ""   # init last to -1 since -1 won't be a char from line
			for c in line.strip():
				if c != last:   # if it is not a repetition
					result += c   # append it to the result str
					last = c   # update pointer to new unique char
			print result

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])