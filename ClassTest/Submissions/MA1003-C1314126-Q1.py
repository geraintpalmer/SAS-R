"""
Class test - question 1
C1314126
The recursive approach is being used to programme the value of Xn for
value of n such that 0<=n<11
"""

def recX(n):
    if n == 1:
        return 1   # So if n = 1, Xn = 0
    if n == 0:
        return 1
    return recX(n - 1) + recX(n - 2)

for n in range (0, 11):
    print recX(n)
