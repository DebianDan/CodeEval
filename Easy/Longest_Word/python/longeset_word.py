import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			longest = ""
			for word in reversed(line.strip().split()):
				if len(word) >= len(longest):
					longest = word
			print longest
			
			

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])