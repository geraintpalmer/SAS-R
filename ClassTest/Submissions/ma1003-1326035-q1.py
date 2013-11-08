
def fib(n):   #defining function 'fibonacci'
    '''operation to code the fibonacci sequence, by using recursion to return the nth
term of the sequence  
    argument:'n', an integer
    output: nth term of fibonacci sequence '''
    if n == 0 or n == 1:  # statements for starting value to check the base case
        return 1   # return call to return a result based on if statement 
    return fib(n - 1) + fib(n - 2)  # Use recursion and the formula for the fibonacci numbers
 
print "The first 10 fibonacci numbers:"

for i in range(11):   # first ten values of fibonacci
    print "f(%s)=%s" % (i, fib(i))


    
