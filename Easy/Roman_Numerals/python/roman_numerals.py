import sys

def main(filename):
	ROMAN_NUMS = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
	with open(filename, 'r') as f:
		for line in f:
			result = ""
			i = int(line.strip())
			for rn in ROMAN_NUMS:
				while i >= rn[1]:
					i -= rn[1]
					result += rn[0]
			print result

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])