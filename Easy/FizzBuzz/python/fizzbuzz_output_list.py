import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			if line.strip() != "":
				x, y, count = [int(num) for num in line.split()]
				output = []
				for num in xrange(1, count+1):
					if (num % x) == 0 and (num % y) == 0:
						output.append("FB")
					elif (num % x) == 0:
						output.append("F")
					elif (num % y) == 0:
						output.append("B")
					else:
						output.append(str(num))
				print " ".join(output)

if len(sys.argv) != 2:
	print "Usage ./fizzbuzz.py <filename>"
	sys.exit(1)
main(sys.argv[1])