"""
Class test - question 1
c13709872
"""

# A function to give the nth fibbonacci number, using n as an integer.

def fib(n):
    if n == 0 or n == 1: 
        return 1 # Both the first and second fibonacci number = 1
    return fib(n - 1) + fib(n - 2) # The rest of the fibonacci sequence are the two previous values added together

print "The fibonacci numbers between 0 and 11:"

for i in range(12): # printing the first 11 numbers
    print "f(%s)=%s" %(i, fib(i))
    
