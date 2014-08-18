"""
Class test - question 1
C1305313
"""

def fibonacci(n):
"""
This function will obtain numbers in the fibonacci sequence in a given range
Argument: n
Output: list of fibonacci numbers
""" 
    if n == 0 or n == 1:  #first two numbers in fibonacci are 1
        return 1
    return fib(n - 1) + fib(n - 2)  #the formula of fibonacci sequence

for i in range(11):  #giving argument of first ten numbers
    print "f(%s)=%s" % (i, fib(i))
