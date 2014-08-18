"""
Class test - question 1
C1313810
"""


def fib(n):
    """
    Function:  this function uses a recursive techinique to fine the nth number in the fibonacci sequence

    Arguments: any integer (n)

    Outputs: the nth fibonacci number in the fibonacci sequence
    """
    if n == 0 or n == 1:  # check whether n is equal to 0 or 1, as the output depends on this (checking base case)
        return 1
    return fib(n - 1) + fib(n - 2)  # using the formula for the fibonacci sequence and recursion, calculate the fibonacci number


for i in range(11):  # print the first 10 fibonacci numbers
    print "f(%s)=%s" % (i, fib(i))

