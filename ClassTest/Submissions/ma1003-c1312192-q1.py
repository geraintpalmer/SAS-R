"""
Class test - question 1
c1312192
"""

def fib(n):
    """
    A function that gives the nth fibonacci number that uses recursion

    Arguments: n, an integer

    Outputs: the nth fibbonacci number
    """
    if n == 0 or n == 1: # Checks base case
        return 1
    return fib(n - 1) + fib(n-2) #Using the formula for the fibonacci numbers and recursion

print "Xn for 0 <= n < 11:"

for i in range(11): # Prints Xn for 0 <= n < 11
    print "f(%s)=%s" % (i,fib(i))
