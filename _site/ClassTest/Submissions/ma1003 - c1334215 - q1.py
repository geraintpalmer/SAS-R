"""
Class Test - Question 1
C1334215
"""

def fibonacci(n):
    """
    A funhction to return Xn using recursiv approach
    Arguments (n) an integer
    Outputs intergers
    """
    if n == 0 or n == 1: #initial values
        return 1
    a = 1  # Setting two values that will be used to hold information in fibonacci calculation
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b  
        i += 1
    return a
 
for i in range(11):  #range < 11
    print fibonacci(i) 
