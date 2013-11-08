def fib(n):

    """
    A function to give the nth fibonacci number using recursion
    arguments: n, an intgar
    outputs: the nth fibonacci number        
    """

    if n == 0 or n == 1:  # Check the base case
      return 1
    return fib(n - 1) + fib(n - 2) # use recursion and the formula for fibonacci numbers

print "The first 10 fibonacci numbers:"
for i in range(11):  # Printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i))


    
