import sys

##############################################################
# MODIFIED to Generate a sequence of prime numbers < n
# Example of an efficient Sieve Prime Number Generator
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes(n):
    """ MODIFIED to Generate a sequence of prime numbers < n
        Generate an infinite sequence of prime numbers.
        http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while q < n:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1



def main(filename):
    # Could improve and store the result of a primes < n
    # for future lookups instead of reGenerating just do a lookup
    with open(filename, "r") as f:
        for line in f:
            n = int(line.strip())
            p = gen_primes(n)
            res = ""
            try:
                while True: 
                    res += str(p.next()) + ","
            except Exception, e:
                print res[:-1]

            
            
if len(sys.argv) != 2:
    print "Usage", sys.argv[0], "<filename>"
    sys.exit(1)
main(sys.argv[1])