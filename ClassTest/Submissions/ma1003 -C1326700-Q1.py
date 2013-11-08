"""
CLASS TEST - QUESTION 1
c1326700
"""

def fib(n):  
    if n == 0 or n == 1:  
        return 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11):  # Printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i)) 
