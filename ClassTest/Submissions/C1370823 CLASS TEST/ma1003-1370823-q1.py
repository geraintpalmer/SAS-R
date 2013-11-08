"""
Class test - question 1
c1370823

"""


def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:  # Check the base case
        return 1  # Returning 1 if n is 0 or 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11):  # Printing the first 10 numbers
    print "fib(%s) = %s" % (i, fib(i))  # Printing information in a clear way
