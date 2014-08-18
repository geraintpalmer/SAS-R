"""
Class test - question 1
c1322758
"""
def fib(n):
    """
    A function that gives the  fibonacci sequence using recursion
    Arguements: n, an integer, between 0 and strictly less than 11
    Outputs : the fibonacci sequence between 0 and 11
    """
    if n == 0 or n == 1:  # checks the base case
        return 1
    
    return fib(n - 1) + fib(n - 2)  #uses recursion and the formula for fibonacci numbers

for i in range(11):
    print "f(%s) = %s" % (i, fib(i))  #  prints the first 10 fibonacci numbers
    

    


