"""
Class test - question 1
c1319433
"""

def fibonacci(n):
    if n == 0 or n == 1: 
        return 1
    a = 1  # setting two values that will be used to hold information in fibonacci calculation
    b = 1
    c = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a

 for i in range(10):
     print fibonacci(i)
