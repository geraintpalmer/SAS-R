"""
Class test - question 1
C1313466
"""

def fibonacci(n):
    if n == 0 or n == 1:  #If n is 0 or 1
         return 1  #Value is 1
    a = 1  # Setting two values that will be used to hold information in fibonacci calculation
    b = 1
    i = 0
    while i < n:  #If i is less than n
        a, b = b, a + b
        i += 1  #Increment i by 1
    return a

for i in range(10):  #All values for i between 0 and (11-1)
    print fibonacci(i)
    

