import sys

def main(filename):
	with open(filename, "r") as f:
		last = -1
		for line in f:
			line = line.strip()
			pos = line.find("C")
			if pos == -1:
				pos = line.find("_")
			if pos == last or last == -1:
				c = "|"
			elif pos < last:
				c = "/"
			elif pos > last:
				c = "\\"
			print line[:pos] + c + line[pos+1:]
			last = pos

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])