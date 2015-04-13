import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			zeros, bin = line.strip().split(), ""
			for i in range(len(zeros)):
				if i % 2 == 0:
					if zeros[i] == "0":
						bin += zeros[i+1]
					elif zeros[i] == "00":
						bin += "1"*len(zeros[i+1])
			print int(bin, 2)


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])