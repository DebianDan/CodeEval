from math import pow, sqrt
from sys import argv
with open(argv[1], 'r') as f:
	for line in f:
		n = int(line.strip())
		print int((1/sqrt(5)) * (pow((1+sqrt(5))/2,n) - pow((1-sqrt(5))/2,n)))
