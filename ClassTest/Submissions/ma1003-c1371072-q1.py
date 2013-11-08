"""
Class Te3st - question 1
c1371072
"""


def iterX(n): #a function to give the sequence defined using an iterative approach
    r = 1 #setting a dummy variable
    for i in range(n-1 + n-2): 
        return r
    
def recX(n):
    """
a function to give the sequence defined using a recursive approach

Arguments: n, an integer
    """
    if n == 0 or n == 1: #identify the base case
        return 1
    
    else:
        return (n-1) +(n-2)

print recX(11)    
