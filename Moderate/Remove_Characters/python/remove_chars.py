import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			text, chars = line.strip().split(", ")
			result = ""
			for c in text:
				if c not in chars:
					result += c
			print result

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])