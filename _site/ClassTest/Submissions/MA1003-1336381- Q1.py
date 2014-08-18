#Exam question 1.


def Fib(n):
    """
    a function to give the nth fibonacci number using recdursion.
    
    Arguments: n, an integer.
    
    Outpoints: the nth fibonacci number.
    """
    
    if n == 0:   # Checks the base case.
        return 1 # If n = 0 then this gives us 1.
    if n == 1:   # Checks another base case.
        return 1 # If n = 1 then this gives us 1.
    return Fib(n - 1) + Fib(n - 2) # Using Recursion and the Formula given for the Fibonacci numbers.

for i in range (1, 11):  # This gives a range to use in the above definition. ( 1 <= N <= 11)
    print Fib(i)   # Prints to Screen Fibonacci numbers.
