'''
class test
question 1
c1226574
'''

def fib(n):
    ''' function which enables recursion for fibonnaci
input: range of integers
output: previous value added to current value for next value
'''
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n-2) + fib(n-1)

for i in range (11):
    print fib(i)
