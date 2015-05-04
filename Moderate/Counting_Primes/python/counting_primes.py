import sys

def make_prime(i):
	while True:
		if all(i%j for j in xrange(2,int(i**0.5+1))):
			yield i
		i+=1

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			n,m = map(int, line.strip().split(","))
			count = 0
			p = gen_primes(n)
			while p.next() <= m:
				count += 1
			print count
				

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])