import sys

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			x,n = map(int, line.strip().split(','))
			m = 0
			while m*n < x:
				m+=1
			print m*n

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])