"""
Class test - question 1
C1318352
"""

def fibonacci(n):
    """
    Using the recursion approach to find the nth fibonacci number.
    
    Arguments: n, an integer
    
    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:  # Incuding the base cases for the fibonacci numbers.
        return 1
    return fibonacci(n-1) + fibonacci(n-2)  # Using recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers are:"

for a in range(11):  # Printing the first 10 fibonacci numbers
    print "f(%s)=%s" % (a, fibonacci(a))
