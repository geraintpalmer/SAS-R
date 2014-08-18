"""
class test - question 1
c1351926
"""

def fib(n):
        """
arguemnts : 'n' will represnet the nth term of the fib sequence.

outputs : n + rec(n-1) +.... *rec(1) = will give nth term of the fib sequence ,
it will return 0 if n = 0
it will return 1 if n = 1

"""
        if n == 0:
                return 0
        if n == 1:
                return 1
        return fib(n-1) + fib(n-2)
                

         
for n in range (11):
        print "%ith fib term=" % (n), fib(n)
