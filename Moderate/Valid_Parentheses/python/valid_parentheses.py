import sys

def main(filename):
	closing = {"(":")", "[":"]", "{":"}"}
	with open(filename, "r") as f:
		for line in f:
			stack = []
			for c in line.strip():
				if c == "(" or c == "[" or c == "{":
					stack.append(c)
				else:
					if len(stack) == 0 or closing[stack.pop()] != c:
						print False
						break
			else:
				if len(stack) == 0:
					print True
				else:
					print False
			

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])