'''
Class test - question 1
c1325348
'''

def fib(n):
    """
    This creates a function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:  # Check the base case
        return 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11):  # Printing numbers between 0 and 10
    print "f(%s)=%s" % (i, fib(i))
