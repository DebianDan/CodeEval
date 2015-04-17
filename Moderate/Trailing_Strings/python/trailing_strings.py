import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			text, word = line.strip().split(",")
			index = text.find(word)
			if index != -1 and index+len(word) == len(text):
				print 1
			else:
				print 0

			

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])