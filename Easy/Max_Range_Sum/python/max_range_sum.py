import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			n, days = [l.strip() for l in line.split(";")]
			days = [int(day) for day in days.split()]
			n = int(n)
			total = 0
			for i in xrange(len(days)-n+1):
				sliding_sum = sum(days[i:i+n])
				if sliding_sum > total:
					total = sliding_sum
			if total <= 0:
				total = 0
			print total


if len(sys.argv) != 2:
	print "Usage ./max_range_sum.py <filename>"
	sys.exit(1)
main(sys.argv[1])