"""
Class test - question 1
c1322189
"""

def fib(n):

"""
This function calculates the nth number in the fibonacci sequence.
It uses the base values of when n = 1 or 2 to make it possible to calculate
any fibonacci number
"""

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range (1, 12):  # This prints all the fibonacci numbers from n = 1 to n = 11
    print fib(i)
