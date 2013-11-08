"""
Class test - question 1
C1302976
"""


def fib(n):
    """
    This is a function that will find me the nth fibonacci number using the recursion method

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:  # Check the base case
        return 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers

print "The first 11 terms of the fibonacci sequence are:"

for i in range(11):  # Printing the first 11 numbers as the range(11) goes from 0 to 10
    print "f(%s)=%s" % (i, fib(i))
