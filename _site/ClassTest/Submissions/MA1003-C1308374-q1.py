"""
Class Test - question 1
c1308374
"""


def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2) # Using recursion and the formula for fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11): # printing the first 10 numbers
    print (i, fib(i))
