"""
Class test - question 1
C1370884
"""

def fib(n): # defining the function fib(n)
    if n == 0 or n == 1:
        return 1 # If n is equal to 0 or 1 print 1
    a = 1
    b = 1
    i = 0 # starting values
    while i < n: 
        a, b = b, a + b # To work out the next value
        i += 1 # The next Xn
    return a

list = [fib(e) for e in range(11)] # The range of values I want printing
print list # Printing the list
