import sys

def fib(n):
	if n > 1:
		return fib(n-1) + fib(n-2)
	return n

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			n = int(line.strip())
			print fib(n)

if len(sys.argv) != 2:
	print "Usage ./fib_n.py <filename>"
	sys.exit(1)
main(sys.argv[1])