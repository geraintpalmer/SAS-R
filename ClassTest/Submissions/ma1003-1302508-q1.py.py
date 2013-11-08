"""
    class test
    c1302508
"""

def fib(n):
"""
a fucntion that gives the nth fibonacii number

arguments: n (an interger)

output: the corresponding fobonacci number (n)

"""
    if n== 0 or n == 1:    # Creates a base case for the start of the recurrsion
        return 1
    return fib(n - 1) + fib(n - 2) # uses recursion to repeat previous fibonacii values

print "The first 10 fibonacii numbers:"

for i in range (11):  # printing the first 10 fibonacii numbers
    print "fibonacii(%s) = %s % (i, fib(i))
