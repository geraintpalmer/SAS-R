"""
Class test - question 1
C1302175
"""

def fib(n):
    """
    A function to give the Fibonacci sequence using a recursive approach

    Arguments: n, an integer

    Outputs: Xn where Xn is defined as Xn-1 + Xn-2
    """

    if n == 0 or n == 1:  #identify the base case
        return 1
    else:
        return (fib(n-1) + fib(n-2))  #return Xn-1 + Xn-2 using the function itself

for i in range(10): #Visualise output of function
    print fib(i)


