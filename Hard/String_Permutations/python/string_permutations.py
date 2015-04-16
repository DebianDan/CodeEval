import sys
from itertools import permutations

with open(sys.argv[1], "r") as f:
    for line in f:
        perm_it = permutations(line.strip())
        str_perms = [p for p in perm_it]
        print ",".join(["".join(x) for x in sorted(str_perms)]) #join each tuple -> str, then join all strs