import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			pos = line.find(".")
			d = line[:pos]
			frac = float(line.strip()[pos:])
			m = int(frac*60)
			s = int((frac - m/60.0)*3600)
			print "{}.{:02d}'{:02d}\"".format(d, m, s)

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])