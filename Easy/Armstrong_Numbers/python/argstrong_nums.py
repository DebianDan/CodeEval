import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			number = int(line.strip())
			power, total = len(line.strip()), 0
			for num in line.strip():
				total += int(num)**power
			if total == number:
				print True
			else:
				print False


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])