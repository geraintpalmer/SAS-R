from scipy import integrate

# This is the function we will integrate.
def myfunc(x, a, b):
return (1 - x*2)
  return 1.
    else:
        return 0.

 
# These are the arguments that will be passed as a and b to myfunc()
args = (1.0, 0.0)      # interval of the integration
 
# Integrate myfunc() from 0.0 to 1.0

results = integrate.quad(myfunc, 0.0, 1.0, args)
print 'Integral = ', results[0], ' with error = ', results[1] 
