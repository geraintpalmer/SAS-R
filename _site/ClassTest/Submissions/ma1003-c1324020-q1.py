# Class test question 1
#C1324020




def fib(n):
    """
    This function will generate the nth fibonacci number using recursion
    Arguments: n, is an integer
    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:    #checks the base case
        return 1
    return fib(n - 1) + fib(n - 2) #Uses recursion and the formula for the fibonacci numbers
print "The first 10 fibonacci numbers:"

for i in range(11): #prints only the first 10 numbers as 11 is not included in the range
print 'f(%s)=%s' %(i, fib(i))

