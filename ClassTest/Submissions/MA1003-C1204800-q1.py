"""
Class test - question 1
C1204800
"""
 
def fib(n):
    if n == 0 or n == 1:  # Assigning initial values for the function
        return 1
    a = 1  # a and b are used to hold information for the fibonacci calculation
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a
 
for i in range(11):  # for fibonacci series between n=0 and n=10
    print fib(i)

"""
Attributes: Initial values for n = 0 and n =1 is 1.
n from 2 to 10.

Outputs: The fibonacccci sequence from n = 0 to n=10
This is, using the initial values for n = 0 and n = 1 to
ouput the fibonacci sequence from 0 to 10, ie. adding the
first two terms to get the third and so on.
"""
