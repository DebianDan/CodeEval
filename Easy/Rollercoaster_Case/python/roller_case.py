import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			case = True
			text = line.strip()
			result = ""
			for c in text:
				if c.isalpha():
					if case:
						result += c.upper()
					else:
						result += c.lower()
					case = not case
				else:
					result += c
			print result
			

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])