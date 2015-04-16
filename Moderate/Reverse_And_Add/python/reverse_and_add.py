import sys

def reverse_and_sum(y):
	num1 = int(y)
	num2 = int(y[::-1])
	return num1 + num2
 
def isPalindrome(str_num):
	for i in range(len(str_num)/2):
		if str_num[i] != str_num[-(i+1)]:
			return False
	return True

def find_palindrome(x, depth):
	depth += 1
	new_sum = reverse_and_sum(x)
	if isPalindrome(str(new_sum)):
		return depth, new_sum
	return find_palindrome(str(new_sum), depth)

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			n = line.strip()
			depth, new_sum = find_palindrome(n,0)
			print depth, new_sum

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])