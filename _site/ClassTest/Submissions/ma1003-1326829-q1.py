"""
Class Test - Question 1
C1326829
"""

def fib(n):
    """
    This function recursively computes and returns the nth term in the Fibonacci sequence

    Input: n - where n is any natural number

    Output: The nth term of the Fibonacci sequence 
    """
    if n == 0 or n == 1:            #F0 and F1 are the only terms in the FIbonacci sequence not defined by Fn = Fn-1 + Fn-2, so these values of n must be dealt with seperately
        return 1                    #becauseF0 and F1 = 1
    return fib(n - 1) + fib(n - 2)  #Recursively calls the function again this time for Fn-1 and Fn-2.

for i in range(11): # For loop Fibonacci term for 0 <= i < 11. The range uses the argument 11 as it the 11 is not inclusive of the range. And the default start value in the range function is 0.
    print fib(i)    # Prints the ith Fibonacci term

