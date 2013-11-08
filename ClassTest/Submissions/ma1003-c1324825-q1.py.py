"""
class test - question 1
c1324825
"""
def fib(n):
    """
this will work out the fibonacci numbers using recursion

Arguments: n , an intiger

outputs: the nth fibonnacci number
    """
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2) #the formula for the fibonacci numbers
print "the first 10 fibonacci numbers:"

for i in range(11):
    print (i, fib(i)) #this prints which number it is in the sequence as well as the actual number calculated
    
