def fib(n):
    """
    Function to give the nth fibonacci number using recursion
    Arguments: n, an integer
    Outouts: the nth fibonacci number
    """
    if n == 0 or n == 1:  # check the base case
        return 1
    return fib(n - 1) + fib(n - 2)  # use recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11):  # printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i))
