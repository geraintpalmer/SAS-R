"""
Class test - question 1
c1306213
"""

def fibonacci(n):
    if n == 0 or n == 1:  # Initial values
        return 1
    a = 1
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a

for i in range (11):
    print fibonacci(i)
