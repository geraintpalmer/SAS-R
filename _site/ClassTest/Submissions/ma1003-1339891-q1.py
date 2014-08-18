"""
Class test - Question 1
C1339891
"""

def recX(n):
    if n == 0:      #check if n = 0
        return 1    #return 1
    if n == 1:      #check if n = 1
        return 1    #return 1
    return recX(n - 1) + recX(n - 2)    #return the sum of the previous two terms

"""
This is a recursive function used to calculate the fibonacci sequence.

Arguments:
    n for the values (0 < n < 11)

Output:
    the sum of the two previous terms, up to 10
"""

print recX(10)  #returns the first 10 terms
