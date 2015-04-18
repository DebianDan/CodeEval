import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			coordinates = map(int, line.strip().split())
			o_p = (coordinates[0], coordinates[1])
			q_r = (coordinates[2], coordinates[3])
			res = ""
			if o_p == q_r:
				print "here"
				continue
			# handle N and S
			if o_p[1] < q_r[1]:
				res += "N"
			elif o_p[1] > q_r[1]:
				res += "S"
			# handle E and W
			if o_p[0] < q_r[0]:
				res += "E"
			elif o_p[0] > q_r[0]:
				res += "W"
			print res


if len(sys.argv) != 2:
	print "Usage",sys.argv[0],"<filename>"
	sys.exit(1)
main(sys.argv[1])