def fib(n):
    """
    this functions finds the nth fibonacci number using the method of recursion

    arguments: n, which is an interger

    outputs: the nth fibonacci number from n=0 to n<11
    """
    if n==0 or n==1:# check base case
        return 1
    return fib(n-1) + fib(n-2)# recursion formula for fibonacci
print "the first 10 fibonacci numbers:"

for i in range(11):#first 10 numbers
    print "f(%s)=%s" %(i, fib(i))
