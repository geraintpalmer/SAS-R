"""
Class test - Question 1
c1320366
"""

def fibonacci(n):
    if n == 0 or n == 1: # Returning 1 for values n = 0 or n = 1, giving an initial value. Special case
        return 1
    a = 1
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b # Swapping the values using simultaneous assignment
        i += 1 # i acts as the counter, giving us the amount of terms we want, in this case 11.
    return a
for i in range(11): # Gives us the first 11 terms of the fibonacci sequence
    print fibonacci(i)

 # calculating the Fibonacci sequence up to the 11th term
