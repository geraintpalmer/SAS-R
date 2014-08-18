"""

Class test - question 1
C1305954

"""

def fib(n):   
    if n == 0: #telling the program what to return for the first fibonacci number
        return 1
    if n == 1:
        return 1 
    return fib(n - 1) + fib(n - 2) #Adding the previous two numbers together to find the next number in the sequence.

"""

A function to produce the first n fibonacci numbers, using recursion

Arguments: n - an integer

Output: The first n fibonacci numbers.

"""

for i in range (10): #Finds the first ten fibonacci numbers.
    print fib(i)
