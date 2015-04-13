import sys

MAX_DEPTH = 20

def isHappy(n, depth):
	# increment depth counter
	depth += 1

	if n == 1:
		return 1
	elif depth == MAX_DEPTH:
		return 0

	sum_squares = 0
	while n:
		sum_squares += (n%10)**2
		n /= 10
	return isHappy(sum_squares, depth)


def main(filename):
	with open(filename, "r") as f:
		for line in f:
			print isHappy(int(line.strip()), 0)


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])