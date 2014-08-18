

def fib(n):
    
    """
    This function recursively computes the fibonacci numbers in the fibonacci sequence.

    Arguments: n

    Output: numbers in the fibonacci sequence
    """
    
    if n == 0 or n == 1:  
        return 1  # This returns 1 when n is equal to 1 or 0
    a = 1
    b = 1
    i = 0
    while i < n:  # While i is less than n, continue through while loop
        a, b = b, a + b  
        i += 1  # Adds one to i and repeats the process
    return a

for i in range(10):  # Denotes the range
    print fib(i)  # Print the first ten fibonacci numbers
