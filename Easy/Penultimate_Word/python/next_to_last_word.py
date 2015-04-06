import sys

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			print line.split()[-2]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: <filename>"
        sys.exit(1)
    main(sys.argv[1])