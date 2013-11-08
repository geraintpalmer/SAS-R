"""
Class test question 1
c1323636
"""

def fib(n):   # defining the function as fibonacci sequence
    """
    A function to give the nth fibonacci number using recursion

    Arguements: n, an interger

    Outputs: the nth fibonacci number
    """
if n == 0 or n == 1: # check for a base case
     return 1
return fib(n - 1) + fib(n - 2) # use recursion method and the fibonacci seqence formula

print "The First 10 Fibonacci Numbers:"

for i in range(11): #printing fibonacci numbers in the value 0 (strictly more that or equal to) and (strictly less than) 11.
    print "f(%s)=%s2" % (i, fib(i))
