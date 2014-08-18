def fib(n):

    #A function to give the nth fibonacci number using recursion
    #Arguments are n, an integer
    #Outputs are the nth fibonacci number
    
    if n == 0 or n == 1:  #Check the base case
        return 1
    return fib(n-1) + fib(n-2)  #Use recursion and the formula for fibonacci numbers

print 'The First 10 Fibonacci numbers.'
for i in range (11):
    print 'f(%s) = %s' % (i, fib(i))  #Print the first 10 numbers in the function
