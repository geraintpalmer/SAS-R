"""
Class Test - Question 1
C1304645
"""

def fibonacci(n):  #define a function to represent the fibonacci sequence
    """
    A function to return the fibonacci sequence using the recursive approach 
    Arguments: n = 0 or n = 1
    Output:  the fibonacci sequence nos 1 to 11
    """
    if n==0 or n==1:
        return 1  # starts with a if loop if n = 0 or 1
    a = 1
    b = 1
    i = 0  #creates variable i
    while i < n:  #if i is less than n
        a, b = b, a+b  #if a and b are equal to b add together and then add one to i 
        i += 1  # this creates a counter
    return a
for i in range (12):  #prints up to the 12th number but not including this number 
    print fibonacci(i)
