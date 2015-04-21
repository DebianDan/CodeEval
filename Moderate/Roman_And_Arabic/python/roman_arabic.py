import sys

def main(filename):
	ROMAN_NUMS = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
	with open(filename, 'r') as f:
		for line in f:
			last_rom = ROMAN_NUMS[line[1]]
			last_value = int(line[0]) * last_rom
			result = 0
			for i in range(2,len(line.strip()), 2):
				num = int(line[i])
				rom_value = ROMAN_NUMS[line[i+1]]
				if rom_value > last_rom:
					result -= last_value
				else:
					result += last_value
				last_rom = rom_value
				last_value = num * rom_value
			# always add the last value
			result += last_value
			print result

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])