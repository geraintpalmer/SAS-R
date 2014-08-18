"""

Class test = question 1
C1323611

"""

def fib(n):

"""
Arguments: n, which is an integer

Outputs: the nth fibonacci number
"""

    if n == 0 or n == 1: # checking base case
        return 1
    return fib(n - 1) + fib(n - 2)
print "The first 10 fibonacci numbers:"
for i in range(11): # first 10 numbers
    print "f(%s)=%s" % (i, fib(i))
