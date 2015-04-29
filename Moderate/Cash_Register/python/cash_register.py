import sys

CURRENCY = ((10000, 'ONE HUNDRED'), (5000, 'FIFTY'), (2000, 'TWENTY'), (1000, 'TEN'), (500, 'FIVE'), (200, 'TWO'), (100, 'ONE'), (50, 'HALF DOLLAR'), (25, 'QUARTER'), (10, 'DIME'), (5, 'NICKEL'), (1, 'PENNY'))

def main(filename):
	with open(filename, 'r') as f:
		for line in f:
			price, payment = map(float, line.split(";"))
			price = int(price*100) #convert to cents
			payment = int(payment*100) #convert to cents
			change = payment - price
			if change < 0:
				print "ERROR"
				continue
			if change == 0:
				print "ZERO"
				continue
			result = ""
			for coin in CURRENCY:
				while change >= coin[0]:
					change -= coin[0]
					result += coin[1] + ","
				if change == 0:
					break
			print result[:-1] #everything but the trailing comma


if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "<filename>"
	sys.exit(1)
main(sys.argv[1])