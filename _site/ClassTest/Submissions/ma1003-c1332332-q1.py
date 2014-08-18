"""
Classtest - question 1
c1332332
"""

def fib(n):
    """
    a function to give the nth fibonacci number using recursion

    arguments: n, an integer

    Outputs: the nth fibonacci number
    """
    if n == 0 or n == 1:  #check the base case
        return 1
    return fib(n - 1) + fib(n - 2)  #use recursion and the fomula for the fibonacci numberes

print "The first 10 fibonacci numbers:"

for i in range(11):  #printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i))
