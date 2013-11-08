"""
Class test - question 1
c1334728
"""

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

for i  in range(0, 11):
    print fib(i)
