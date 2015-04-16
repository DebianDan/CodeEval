import sys
from math import ceil

def log2n_number_guess(n, master):
	lower = 0
	upper = n
	guess = ceil(n/2.0)
	for response in master:
		if response == "Yay!":
			return int(guess)
		elif response == "Lower":
			upper = guess - 1
		elif response == "Higher":
			lower = guess + 1
		guess = ceil(lower + ((upper-lower)/2.0))


def main(filename):
	with open(filename, "r") as f:
		for line in f:
			user_input = line.strip().split()
			n = int(user_input[0])
			master_responses = user_input[1:]
			print log2n_number_guess(n, master_responses)


if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])