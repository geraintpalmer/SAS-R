"""
class test - Question 1
c1300086
"""

def fib(n):


    """     A function to give the nth fibonacci number using recursion    """
    if n == 0 or n == 1:  # Check the base case eg if n is 0 or 1 return 1
        return 1
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers

print "The first 10 fibonacci numbers:"

for i in range(11):  # Printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i)) 
