"""
solution to question 1 of class test

"""

def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """

    if == 0 or n == 1:  # Check the base case
        return 1
    return fib(n-1) +fib(n-2) # Use recursion and the fibonacci formula

print "The first 10 fibonacci numbers:"

for i in range(11): # printing the first ten numbers
    print "f(%s)=%s" %(i, fib(i))
    
