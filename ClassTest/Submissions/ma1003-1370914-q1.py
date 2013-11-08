def fib(n):
    """
    A function to give the nth fibonacci number using recursion

    Arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:  # Check the base case for n = 0, or n = 1
        return 1  # Return 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11):  # For numbers i up to 11
    print "f(%s)=%s" % (i, fib(i))  # Print f(n) = the corresponding Fibonacci number
