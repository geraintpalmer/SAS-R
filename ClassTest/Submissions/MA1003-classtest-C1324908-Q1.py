def fib(n):
    """
    This is a recursive function that determines the nth Fibonacci number

    Arguments: n, an integer

    Outputs: the nth Fibonacci number
    """
    if n == 0 or n == 1:  # Check the base case
        return 1
    return fib(n-1) + fib(n-2)  # Use the recursive Fibonacci formula

for i in range(11):  # Prints the first 10 Fibonacci numbers
    print "f(%s) = % s" % (i, fib(i))
