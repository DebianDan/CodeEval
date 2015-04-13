import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			if len(line.strip()) == 0:
				continue
			enc, keys = line.strip().split("|")
			keys = map(int, keys.split())
			writer = ""
			for key in keys:
				writer += enc[key-1]
			print writer


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])