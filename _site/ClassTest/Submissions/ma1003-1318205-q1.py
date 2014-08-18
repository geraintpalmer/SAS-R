def fibonacci(n): #defining the function as fibonacci
    if n == 0 or n == 1: 
        return 1 # it will return 1 if n is 1 or 0
    a = 1 
    b = 1
    i = 0 # giving variables a, b and i values
    while i < n:
        a, b = b, a + b # this is the job of the function
        i += 1          # incriment i
    return a            # function will then return a
for i in range(10):     # for 0 <= n < 11
    print fibonacci(i)  # print 
