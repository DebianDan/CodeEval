for i in xrange(1, 13):
	for j in xrange(1, 13):
		#print '%3s' % (i*j),  #Alternate String Formatting
		print '{0:>3}'.format(i*j), #3 since , is printing out an extra space
	print '\n'