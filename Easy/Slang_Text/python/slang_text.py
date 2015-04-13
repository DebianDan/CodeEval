import sys

def main(filename):
	slang = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?", ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"]
	with open(filename, "r") as f:
		text = f.read()
		punc_flag, slang_cur, res = 0, 0, ""
		for c in text:
			if c == "." or c == "?" or c == "!":
				if punc_flag:
					res += slang[slang_cur]
					slang_cur += 1
					if slang_cur == 8:
						slang_cur = 0
				else:
					res += c
				punc_flag = abs(punc_flag-1)
			else:
				res += c
		print res

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])