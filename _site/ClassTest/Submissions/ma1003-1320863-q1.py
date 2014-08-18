"""
Computing for mathematics
Class test
Solution to Q1
"""
 
def fib(n):
    if n == 0 or n == 1:  # The function needs an 'initial' value
        return 1
    a = 1  # Setting two values that will be used to hold information in fibonacci calculation
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b  
        i += 1 
    return a
 
for i in range(11):  # Visualise output of function
    print fib(i)
 
