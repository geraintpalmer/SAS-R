"""
Class test - question 1
c1318875
"""

"""
the fibonnaci sequence using a recursive approach
"""

def fibonacci(n):
    if n == 0 or n == 1: #giving the function a 'intial' value
        return 1 #in this case output the number 1
    a = 1 #setting two values thast will be used to hold information in fibonacci calculation 
    b = 1
    i = 0
    while i < n:
        a,b = b, a + b
        i += 1
    return a

for i in range(11): #use the function to print the answers to n in the range between 0 and 11
    print fibonacci(i)
    
