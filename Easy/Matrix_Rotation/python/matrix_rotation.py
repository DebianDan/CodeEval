import sys

def create_matrix(line):
	"""
	Creates an NxN matrix from serialized text input 
	"""
	lst = line.split()
	n = int(len(lst)**.5)
	mat = [lst[i*n:i*n+n] for i in range(n)]

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			lst, res = line.split(), ""
			n = int(len(lst)**.5)
			for i in range(n, 0, -1):
				for j in range(n):
					res += lst[-i-(j*n)] + " "
			print res[:-1] #trim off last space

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])