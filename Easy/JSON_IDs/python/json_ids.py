import sys
import json

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			total = 0
			for item in json.loads(line)["menu"]["items"]:
				if item:
					if "label" in item:
						total += int(item["id"])
			print total
			
if len(sys.argv) != 2:
	print "Usage ./json_ids.py <filename>"
	sys.exit(1)
main(sys.argv[1])