"""
class test question 1
C13708034
"""

def fib(n):
    """
    a function to give the nth fibonacci number using the recursive approach

    argumens: n, an interger

    output: the nth fibonacci number
    """

    if n == 0 or n == 1:  # to check the base cases
        return 1
    return fib(n - 1) + fib(n - 2)  # using recursion and the formula for fibonacci numbers.

print "The first 10 fibonacci numbers:"

for i in range(11): # printing the first 10 number in the fibonacci sequence.
     print "f(%s)=%s" % (i, fib(i))
