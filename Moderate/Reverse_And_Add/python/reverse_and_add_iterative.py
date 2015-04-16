import sys

def reverse_and_sum(y):
	num1 = int(y)
	num2 = int(y[::-1])
	return str(num1 + num2)
 
def isPalindrome(str_num):
	for i in range(len(str_num)/2):
		if str_num[i] != str_num[-(i+1)]:
			return False
	return True

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			n = line.strip()
			new_sum = reverse_and_sum(n)
			depth = 1
			while not isPalindrome(new_sum):
				depth += 1
				new_sum = reverse_and_sum(new_sum)
			print depth, new_sum

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])