import sys

def main(filename):
	with open(filename, "r") as f:
		num = int(f.readline())
		text = f.read()
		line_list = text.split("\n")[:-1] # peel off the last '' element
		sorted_lines = sorted(line_list, key=lambda x:len(x), reverse=True)
		longest_lines = sorted_lines[:num]
		print "\n".join(longest_lines)

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])