"""
Class test - question 1
C1339447
"""
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 2
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a

for i in range(0, 11):
    print fibonacci(i)
