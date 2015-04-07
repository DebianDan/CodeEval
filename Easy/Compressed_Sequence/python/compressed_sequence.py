import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			seq = line.split()
			count, num, comp_seq = 0, -1 , []
			for i in seq:
				if num == i:
					count += 1
				else:
					if num != -1:
						comp_seq += [str(count), str(num)]
					num = i
					count = 1
			comp_seq += [str(count), str(num)]
			print " ".join(comp_seq)

if len(sys.argv) != 2:
	print "Usage ./compressed_sequence.py <filename>"
	sys.exit(1)
main(sys.argv[1])