"""
class test - question 1
C1336772
"""

def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    
    if n == 0 or n == 1:        # checking the base case
        return 1
    return fib(n-1) + fib(n-2)  # use recursion and thye formula for the fibonacci numbers

print "the first 10 fibonacci numbers:"

for i in range(11):   # printing the first 10 numbers
     print "f(%s)=%s" % (i, fib(i)) 

    
