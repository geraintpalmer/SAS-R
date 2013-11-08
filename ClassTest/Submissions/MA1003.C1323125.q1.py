def fib(n):

    """
This function gives the nth fibonnaci number using recursion

Arguments: n, an integer

Outputs: the nth fibonacci number

"""
    
    if n== 0 or n== 1:   # checking the base case
        return 1
    return fib(n - 1) + fib(n - 2)  # Using recusion and the formula for fibonacci numbers

for i in range(11):    # printing the first 10 numbers in the sequence
    print "f(%s) = %s" % (i, fib(i))
