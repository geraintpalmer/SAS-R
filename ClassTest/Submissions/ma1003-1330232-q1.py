"""
Class test - question 1
C1330232
"""

def fib(n):
    """
    This is a recursive program for the Fibonacci sequence

    Arguments: n

    Output: a term in the fibonacci sequence depending on n
    """
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

fibonccinumbers = [fib(n) for n in range(0, 11)]
print fibonccinumbers
