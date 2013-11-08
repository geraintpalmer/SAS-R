"""
Class test - question 1
c1316800
"""

"""
This function will list the fibonacci numbers from 1 - n.

Arguments:
    n: the nth value of which the fibonacci sequence will list up to.

output: fibonacci sequence
"""
def fib(n):  # comments had to go above because it wouldnt work below.
    if n == 0 or n == 1:
        return 1
    a = 1  # Setting two values that will be used to hold information in fibonacci calculation
    b = 1
    i = 0
    while i < n:  # creates a loop for when i is smaller than n it repeats
        a, b = b, a + b
        i += 1  # increments i by 1
    return a
    
for i in range(10):  
    print fib(i)   # prints fibonacci up the the 10th value
