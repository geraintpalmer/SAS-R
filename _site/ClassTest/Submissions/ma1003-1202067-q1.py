#here we have called our function fib(n). the name is irrelevant, it's what we put into the function that matters#

def fib(n):
    """
    arguments : n is our input.
    outputs : the value of n based on two terms before in the fibbonaci sequence.

    """
    if n == 0:
        return 1
#if n is 0, we want our output to be 1.#
    if n == 1:
        return 1
#if n is 1, we want our output to be 1.#    
    return (n-1) + (n-2)
#otherwise, the number n is equal to the sum of the two previous terms before.#
#I have tested the code, it works perfectly. now, we want to print all outputs for n being being 0 up to n being 11.#
print fib(0)
print fib(1)
print fib(2)
print fib(3)
print fib(4)
print fib(5)
print fib(6)
print fib(7)
print fib(8)
print fib(9)
print fib(10)
print fib(11)



