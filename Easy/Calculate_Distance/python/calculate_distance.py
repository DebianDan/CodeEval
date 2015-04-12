import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			p1, p2 = [map(int, p.split(", ")) for p in line.strip()[1:-1].split(") (")] # extract both points
			print int(((p2[0] - p1[0])**2+(p2[1] - p1[1])**2)**0.5) # calculate distance
			

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])