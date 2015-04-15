import sys
# Each integer N is 2 <= N <= 18
# Largest sum is 18 + 17 = 35
PRIMES = [2,3,5,7,11,13,17,19,23,29,31] # This represents all possible primes encountered
CIRCULAR = []

def custom_perms(elements):
		if len(elements) <=1:
			yield elements
		else:
			for perm in custom_perms(elements[1:]):
				for i in range(len(elements)):
					# nb elements[0:1] works in both string and list contexts
					p = perm[:i] + elements[0:1] + perm[i:]
					if p not in CIRCULAR:
						yield p
					else:
						CIRCULAR.remove(p)

def all_sum_primes(perm):
	for i in range(-1,len(perm)-1):
		if perm[i]+perm[i+1] not in PRIMES:
			return False
	else:
		return True

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			n = int(line.strip())
			if n % 2 == 1:
				print 0
				break
			beads = range(1, n+1)
			all_perms = custom_perms(beads)
			total_perms = 0
			for p in all_perms:
				p2 = p[:]
				for i in range(len(p)-1):
					p2.append(p2.pop(0))
					CIRCULAR.append(p2[:])
				
				if all_sum_primes(p):
					print p
					total_perms += 1
			
			print total_perms


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])