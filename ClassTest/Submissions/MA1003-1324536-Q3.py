"""

Class test - Question 3
C1324536

"""

def myfunc(x, a, b):
    return 1 - x ** 2
 
args = (1.0, -2.0) # These are the arguments that will be passed as a and b to my func()
 
results = integrate.quad(myfunc, 0, 1, args) # Integrate myfunc() from 0 to 1
print 'Integral = ', results[0], ' with error = ', results[1]

"""

Defined my function
Integrating 1 - x ** 2

"""
