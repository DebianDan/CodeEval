import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			data, hints = [[x for x in lst.split()] for lst in line.strip().split(";")]
			for i in range(1,len(data)+1):
				if str(i) not in hints:
					hints.append(str(i)) 
					break 
			for pair in zip(hints,data):
				data[int(pair[0])-1] = pair[1]
			print " ".join(data)

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])