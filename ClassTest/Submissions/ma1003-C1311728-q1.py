"""
Class test - question 1
C1311728
"""

def fib(n):
    """
    A function to give the neth fibonaaci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """

    if n == 0 or n == 1: # Checks the base case
        return 1
    return fib(n - 1) + fib(n - 2) # Use recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11): # Printing the first 10 numbers
    print "f(%s) = %s" % (i, fib(i))
