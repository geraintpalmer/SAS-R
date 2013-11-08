"""
class test - question 1
c1333365
"""
def recX(n):
    if n == 0: # when n = 0
        return 0
    if n == 1: # when n = 1
        return 1
    return (recX(n - 1) + (recX(n - 2)) # X(n - 1) + X(n - 2)

print recX(0, 11) # print from 0 to 11


