"""
class test - q1
c1308627

"""

def fib(n):
    """
This is a function to give the nth fibonacci number using recursion
arguments: this def takes the arguments n which is any integer
output: the nth fibonacci number
    """

    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print "The first 11 fibonacci numbers"

print fib(12)  # 

for i in range (12):  #the range twelve here means it will print n = 11, range goes from 0 to 11 for
    print "f(%s)=%s" % (i, fib(i))
