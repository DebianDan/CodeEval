import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			raw_list, n = line.strip().split(";")
			n = int(n)
			l = raw_list.split(",")
			l_len = len(l)
			res = []
			j = 0
			for i in range(n,l_len+1,n):
				tmp = l[j:i]
				res.extend(tmp[::-1])
				j = i
			res.extend(l[j:l_len])
			print ",".join(res)				

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])