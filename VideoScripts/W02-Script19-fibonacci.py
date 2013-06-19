def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a

for i in range(10):
    print fibonacci(i)
