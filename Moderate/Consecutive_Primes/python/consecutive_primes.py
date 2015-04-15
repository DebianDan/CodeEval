import sys
from itertools import combinations
# Each integer N is 2 <= N <= 18
# Largest sum is 18 + 17 = 35
PRIMES = [2,3,5,7,11,13,17,19,23,29,31] # This represents all possible primes encountered

def all_sum_primes(perm, n):
	if len(perm) != n:
		return False
	if perm[0]+perm[-1] not in PRIMES:
			return False
	else:
		return True

def find_perms(combs, n):
	all_perms = []
	starts = [[y for y in x] for x in combs]
	i = 0
	while i < len(starts):
		#print starts
		temp_p = starts[i]
		#print "TEMP:",temp_p

		for _slot in range(len(temp_p), n):
			option = []
			for c in combs:
				if c[0] == temp_p[-1]:
					if c[1] not in temp_p:
						option.append(c[1])
				elif c[1] == temp_p[-1]:
					if c[0] not in temp_p:
						option.append(c[0])
			
			if len(option) > 1:
				for opt in option:
					starts.append(temp_p[:] + [opt])
				options = []
				starts.remove(temp_p)
				i-=1
				break #go on to next start value
			elif len(option) == 1:
				temp_p.append(option[0])

		# Check if start+end is in PRIMES
		if all_sum_primes(temp_p, n):
			if temp_p not in all_perms:
				#print "Appended:",temp_p
				all_perms.append(temp_p)
		i += 1
	return all_perms



def main(filename):
	with open(filename, "r") as f:
		for line in f:
			n = int(line.strip())
			if n % 2 == 1:
				print 0
				break
			beads = range(1, n+1)
			all_combs = combinations(beads,2)
			prime_combs = []
			for com in all_combs:
				if com[0] + com[1] in PRIMES:
					prime_combs.append(com)
			#print "Prime Combinations:",prime_combs

			perms = find_perms(prime_combs, n)
			#print "Perms Returned", perms

			# Remove Rotations
			for ans in perms:
				p2 = ans[:]
				for i in range(len(ans)-1):
					p2.append(p2.pop(0))
					if p2 in perms:
						perms.remove(p2)
			
			#print "Answer:",perms
			print len(perms)



if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])