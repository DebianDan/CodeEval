import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			res = ""
			for c in line.strip():
				o_c = ord(c)
				if c.isdigit():
					res += c
				elif o_c >= 97 and o_c <= 106:
					res += str(o_c-97)
			if not res:
				res = "NONE"
			print res 

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])