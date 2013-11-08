"""

Class test - Question 1
C1324536

"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    a = 1  
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b # adds the previous number every time 
        i += 1
    return a
 
for i in range(11): # will only show the first 10 terms (0 <= n < 11)
    print fibonacci(i)

def recX(n):
    if n == 1:  # base case
        return 1
    return recX(n - 1) + recX(n - 2)

print recX(6)

"""

Recursive approach
When you input argument it checks if base case
If it's true then it'll return the value
If it's false it'll repeat itself

Arguments: Define fibonacci and using Recursion function

Output:Prints Fibonacci sequence 
        
"""
