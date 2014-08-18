"""
Class test - question 1
c1307787
"""
def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Output: the nth fibonacci number
    """

    if n == 0 or n == 1: # check the base case
        return 1
    return fib(n - 1) + fib(n - 2) # use recursion and known fibonacci formula for the fibonacci numbers

for i in range(11):
               print "f(%s) = %s" % (i, fib(i)) # print the first ten fibonacci numbers
