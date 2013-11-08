"""
Class test - question 1
C1353578
"""

def fib(n):
    """
A function to determine the nth fibonacci number
this function will use a recursive approach
"""
    
    if n == 0:
        return 1
    if n == 1:
        return 1
    """"
these lines set the base case
the recursive formula will use these two to determine the values of all subsequent 'n'
"""

    else:
        return fib(n - 1) + fib(n - 2)

"""
final lines use recursion with the fibonacci formula F(n) = F(n - 1) + F(n - 2)
"""

for i in range(1, 10):
    print fib(i)

"""
A test of the recursion, printing the first 10 fibonacci numbers
"""
