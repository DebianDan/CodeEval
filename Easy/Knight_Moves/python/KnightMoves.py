import sys

def pos_str_to_ints(pos_str):
	col = ord(pos_str[0]) - ord("a") + 1
	row = int(pos_str[1])
	return col, row

def ints_to_pos_str(move):
	return chr(ord("a") + move[0]-1) + str(move[1]) 

def calc_next_moves(col, row):
	return [
		(col-2, row-1),
		(col-2, row+1),
		(col+2, row-1),
		(col+2, row+1),
		(col-1, row-2),
		(col-1, row+2),
		(col+1, row-2),
		(col+1, row+2),
	]

def is_on_board(m):
	if m[0]<1 or m[0]>8 or m[1]<1 or m[1]>8:
		return False
	return True

def main(filename):
	 with open(filename, 'r') as f:
	 	for line in f:
	 		pos = line.strip()
	 		col, row = pos_str_to_ints(pos)
	 		next_moves = calc_next_moves(col, row)
	 		valid_moves = []
	 		for move in next_moves:
	 			if is_on_board(move):
	 				valid_moves.append(ints_to_pos_str(move))
	 		print ' '.join(sorted(valid_moves))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: <filename>"
        sys.exit(1)
    main(sys.argv[1])