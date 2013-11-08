"""
Solution to question 21 of week 2 lab sheet.
"""

def fibonacci(n):
    if n == 0 or n == 1:  # Students might struggle with this (realising that the function needs an 'initial' value)
        return 1
    a = 1  # Setting two values that will be used to hold information in fibonacci calculation
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b  # This is an important step and some students might have difficulties with it
        i += 1
    return a

for i in range(12):  # Visualise output of function
    print fibonacci(i)

"""
Ensure that students are able to write those statements (check that they have a brief understanding of what is happening).
"""
