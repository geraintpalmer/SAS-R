# The Fibonacci sequence is 1,1,2,3,5,8,....
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

for i in range(11):
    print fibonacci(i)
#So this code will give me the fibonacci sequence
    # fib(n) needs to be recursive
# the question wants range from 0 or eqal or less than 11
