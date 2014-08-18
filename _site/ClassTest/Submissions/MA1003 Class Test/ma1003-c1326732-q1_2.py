def fib(x):
    """
    A function to give the nth fibonacci number using recursion
 
    Arguments: n, an integer
 
    Outputs: the nth fibonacci number
    """
    if x % 1 != 0 or x < 0:
        return "fibonacci sequence is only valid for positive natural numbers and zero"
    elif x == 0 or x == 1:  # Check the base case
        return 1
    else:
        return fib(x - 1) + fib(x - 2)  # Use recursion and the formula for the fibonacci numbers

for i in range(0,11):  # Printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i))

