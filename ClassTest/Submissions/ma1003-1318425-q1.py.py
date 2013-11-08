def fib(n):
    """
    Defines a function which gives the nth fibonacci number using recursion

    Takes the arguments: n which is an integer

    Outputs: the nth fibonacci number
    """
    
    if n == 0 or n == 1:  # Provides the base case for the function
        return 1
    return fib(n-1) + fib(n-2)  # Uses recursion and the fibonacci formula

print "The values of the fibonacci numbers from f(0) to f(10) inclusive are:"

for i in range(11):  # Prints the first 11 numbers
    print "f(%s)=%s" % (i, fib(i))
