"""
Class test - question 1
C1370388
"""

def fib(n): # defining a function to compute the nth fibonacci number using recursion
    if n == 0 or n == 1: # checking the base case, ie first number of the sequence is 1
        return 1
    return fib(n - 1) + fib(n - 2) # using the formula for fibonacci numbers and recursion 

print "The first 10 fibonacci numbers:"

for i in range(11): # prints the first 10 numbers in the sequence
    print "f(%s)=%s" % (i, fib(i))
