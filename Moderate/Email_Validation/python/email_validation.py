import sys, re
with open(sys.argv[1], 'r') as f:
    for line in f:
        print line
        if re.match(r'\b[a-zA-Z0-9._%+-@"]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b', line.strip()):
            print "true"
        else:
            print "false"