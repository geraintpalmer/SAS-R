def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

'''
takes integer value n
if n is 0 or 1 returns 1
else returns n = the value of n-2 plus the value of n-1
'''

for i in range(0, 12):  #for the values 0 to 11
    print("Fib(%i)=%i") % (i, fib(i))  #print the fibonacci value for n
