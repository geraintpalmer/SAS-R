
def fib(n):
    """
    This is a recursive approach to programming the fibonacci sequence

    Arguments: n, an integer which is the legnth of the sequence/ the number of terms you want

    Outputs: a list of fibonacci numbers up to the (n - 1)th term
    """
    if n == 0 or n == 1:
        return 1  # This returns the first two fibonacci numbers as 1, 1
    return fib(n - 1) + fib(n - 2)  # This creates the next fibonacci numbers up to n (which is specified), by using the previous


print "The first 10 fibonacci numbers are:"


for i in range(11):  # Prints a list of the first 10 fibonacci numbers from 0 to 10
    print "fibonacci(%s)=%s" % (i, fib(i))
