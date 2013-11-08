"""
Class test - question 1
C1338020
"""

def fib(n):
    """
    This function returns the nth number of the fibonacci sequence

    Arguments: n - an integer signifying the term in the sequence you wish to find

    Output: An integer equal to the nth term in the sequence. 
    """
    if (n == 0) | (n == 1):     # If n is either of our base cases return 1
        return 1                
    return fib(n-1) + fib(n-2)  # Else return the sum of the previous two terms in the sequence

print "The fibonacci numbers from 0 <= n < 11 are as follows:"
for i in range(0,11):           # Print the fibbonacci terms from 0-10
    print fib(i)


    
