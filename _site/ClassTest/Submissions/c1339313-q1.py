"""
Class test - question 1
c1339313
"""


def nthprime(n):
"""
Takes a number n, if n is 0, it gives 0.  If n is 1, it gives 1.  Else, it returns the function of n-1 added to the function of n-2
"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nthprime(n-1) + nthprime(n-2)

print [nthprime(i) for i in range(0, 12)]
