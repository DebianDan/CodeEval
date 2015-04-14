import sys
from time import mktime, strptime

PATTERN = "%b %Y"

def main(filename):
	with open(filename, "r") as f:
		for line in f:
			date_ranges, times = [d.split("-") for d in line.strip().split("; ")], []
			for pair in date_ranges:
				t0 = (mktime(strptime(pair[0], PATTERN)), 1)
				t1 = (mktime(strptime(pair[1], PATTERN)), 0)
				times.extend([t0,t1])

			times_ord = sorted(times, key=lambda x: x[0])
			working, total = [], 0
			for i in range(len(times_ord)):
				t = times_ord[i][0]
				start_flag = times_ord[i][1]

				if start_flag:
					working.append(t)
				else:
					if len(working) == 1:
						total += round(((t-working[0]) * 12 / 31556900.0) + 1)
					working.pop()
			print int(total/12)

if len(sys.argv) != 2:
	print "Usage", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])