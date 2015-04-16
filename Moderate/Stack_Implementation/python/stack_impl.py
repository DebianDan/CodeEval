import sys

def noStack(filename):
	with open(filename, "r") as f:
		for line in f:
			nums, res = map(int, line.strip().split()), ""
			flag = 1
			for num in reversed(nums):
				if flag:
					res += str(num) + " "
				flag = abs(flag-1)
			print res[:-1]


class Stack(object):
	def __init__(self):
		self.stack = []
	def __len__(self):
		return len(self.stack)
	def push(self, x):
		self.stack.append(x)
	def pop(self):
		return self.stack.pop()

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			stack = Stack()
			res = ""
			nums = map(int, line.strip().split())
			for num in nums:
				stack.push(num)

			flag = 1	
			for _ in range(len(stack)):
				num = stack.pop()
				if flag:
					res += str(num) + " "
				flag = abs(flag-1)
			print res[:-1]
		

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])