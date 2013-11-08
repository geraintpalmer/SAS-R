"""
    Class test - question 1
    c1301828
"""

def fib(n):
    """
    This function gives the nth fibonacci number using recursion

    Arguments: n which is an integer

    Outputs: the nth fibonacci number (term in the sequence)
    """
    if n == 0 or n == 1:  # This checks the base case
        return 1
    return fib(n - 1) + fib(n - 2)  # Here I used recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11):
    print "f(%s)=%s" % (i, fib(i)) # Prints the first 10 numbers 
