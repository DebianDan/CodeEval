import sys

def main(filename):
	CODE = {'---': 'O', '--.': 'G', '-...': 'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q', '--..': 'Z', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '-.-.': 'C', '..-.': 'F', '-.--': 'Y', '-': 'T', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '.----': '1', '-----': '0', '-.-': 'K', '-..': 'D', '----.': '9', '-....': '6', '.---': 'J', '.--.': 'P', '....-': '4', '--': 'M', '-.': 'N', '....': 'H', '---..': '8', '...-': 'V', '--...': '7', '.....': '5', '...--': '3'}
	
	with open(filename, 'r') as f:
		for line in f:
			words = [word.split() for word in line.strip().split("  ")]
			res = ""
			for word in words:
				for c in word:
					res += CODE[c]
				res += " "
			print res[:-1]	

if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])