"""
Class Test - Question 1
c1315077
"""

def fib(n):
    """
    A function to give the nth fibonacci function using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1: # This checks the base case.
        return 1
    return fib(n - 1) + fib(n - 2) # This uses recursion and the formula for the fibonacci numbers

print"The first 10 fibonacci numbers (In range 0 <= n < 11):"

for i in range(11): # This prints the first 10 (in the range 0 <= n < 11)
    print "f(%s)=%s" % (i,fib(i))
