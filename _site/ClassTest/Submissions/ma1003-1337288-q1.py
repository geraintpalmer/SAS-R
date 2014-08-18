def fib(n):		#Define a function 'fib' which takes the variable n and gives the nth value of the Fibonacci sequence.
	if n == 0 or n == 1:		#Fibonacci terms 0 and 1 are just 0 and 1.
		return n
	else:		#Function calls itself and calculates the sum of n-1 andf n-2 repeatedly to find the Fibonacci number.    
		return fib(n-1) + fib(n-2)

for n in range(11):		#Loops for 0<=n<11 and returns a string with the the number n and its corresponding Fibonacci value.
	print "The %dth/rd number in the Fibonacci sequence is %d.\n" %(n, fib(n))		#Prints a string which takes in the values for n and fib(n).
