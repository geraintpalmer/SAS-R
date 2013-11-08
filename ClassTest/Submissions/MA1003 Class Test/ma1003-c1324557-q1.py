"""
class test - question 1
c1324557
"""

def fibonacci(n):   #defining the function
    if n == 0 or n == 1:

    #the function needs an initial starting value

        return 1
    a = 1
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a

for i in range (10):   #visualise output of the function
    print fibonacci(i)
