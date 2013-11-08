"""
Class Test - Question 1
C1325167
"""

def fib(n): # This defines the function fibonnaci
    if n == 0 or n == 1: # this is stating the inital value of the function
        return 1
    a = 1 # These two values will be used to hold the information in the calvulation
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a

for i in range(0, 11): # this will run the calculation between these two values
    print fib(i) #this will print out the function with the range stated above
