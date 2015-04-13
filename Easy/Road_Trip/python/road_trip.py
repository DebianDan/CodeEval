import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			res = []
			dists = sorted([int(city.strip().split(",")[1]) for city in line.strip().split(";") if city])
			res.append(str(dists[0]))
			for i in range(1,len(dists)):
				res.append(str(dists[i] - dists[i-1]))
			print ",".join(res)


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])