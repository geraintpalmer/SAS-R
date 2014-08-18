"""
Class test-Question 1
c1329547
"""

def fib(n):
    if n==0: # indentify the base sequence
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-1)+ fib(n-2) #return Xn-1 +Xn-2 using the function itself
k= 0
while k<11:     #Q 1 says use the function to print Xn for 0<=n<11
    print fib(k)
    k+=1     # adds 1 to k each time


    
   
