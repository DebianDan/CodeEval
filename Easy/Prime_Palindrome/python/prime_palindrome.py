for i in xrange(999, 2, -2): #only iterate odd nums <1000 since evens aren't prime
	if str(i)[0] == str(i)[-1]: #isolates palindromes
		if all(i%j for j in xrange(2,int(i**0.5+1))): #determine if prime, only go through 1/2 of factors
			print i
			break
"""
Finding the square root of the number is for efficiency. 
eg. if I am trying to find the factors of 36, 
the highest number that can be multiplied by itself to form 36 is 6. 7*7 = 49.

Therefore every factor of 36 has to be multiplied by 6 or a lesser number.

------------------

Consider the number 20; the integer factors are 1, 2, 4, 5, 10, and 20. 
When you divide 20 by 2 and get 10, you know that it is also divisible 
by 10, without having to check. When you divide it by 4 and get 5,
you know it is divisible by both 4 and 5, without having to check for 5.

After reaching this halfway point in the factors, 
you will have no more numbers to check which you haven't 
already recognized as factors earlier. Therefore, you only 
need to go halfway to see if something is prime, and this 
halfway point can be found by taking the number's square root.
"""