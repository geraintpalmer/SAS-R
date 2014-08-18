def fib(n):
    """
    A function to give the nth fibonacci number using recursion.

    Arguments: n, an integer

    Outputs: the nth Fibonacci number.
    """
    
    if n == 0 or n == 1: # Check the base case
        return 1
    return fib(n - 1) + fib(n - 2) # Use recursion and the formula for the fibonacci numbers

for i in range(11):     # This code will print the first 10 numbers of the sequence.
    print (i, fib(i))
