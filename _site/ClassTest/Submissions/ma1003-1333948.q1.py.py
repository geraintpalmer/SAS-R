def fib(n):
    """
    This creates a function to the properties of the fibbonacci sequence
    Where n is an integer
    this then gives the nth term in the fibbonaci sequence
    """
    if n == 0 or n == 1:  # Check the base case
        return 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers 
print "The first 10 fibonacci numbers:"

for i in range(11):  # Printing the first 10 numbers
     print "f(%s)=%s" % (i, fib(i)) 
