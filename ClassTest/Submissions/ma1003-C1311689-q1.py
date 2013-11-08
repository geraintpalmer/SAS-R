"""
Class test - Question 1
C1311689
"""

def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:   #Check the base case
        return 1
    return fib(n - 1) + fib(n - 2) #Use recursion and the formula for the fibonacci numbers

for i in range(11):   # Prints the fist 10 fibonacci numbers
    print "f(%s)=%s" % (i, fib(i))
