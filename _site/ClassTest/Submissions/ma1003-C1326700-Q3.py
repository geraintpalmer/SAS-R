"""
CLASS TEST - question 3
C1326700
"""



class Drop():
    def __init__(self, r=1):
        self.x = (.5 - random.random()) * 1 # value of x coordinate
        self.y = (.5 - random.random()) * 1  #value of y coordinate
        self.undergraph = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2


def myfunc(x, a, b):
    a = 1
    b = 2
return a - (x**b)
 

args = (1.0, -2.0)  # These are the arguments that will be passed as a and b to myfunc()
results = integrate.quad(myfunc, 0, 1, args) # Integrate myfunc() from 0 to 1
print 'Integral = ', results[0], ' with error = ', results[1] 


def approxintegral(N=1000)
    numberofpointsundergraph = 0
    for i in range(N):  # A loop to drop sufficient points
        drop = Drop()  # Generate a new drop
        if drop.undergraph:  # Check if drop is in under the graph
            numberofpointsundergraph += 1
    return 4 * numberofpointsundergraph / float(N)


print "For N=200, integral approximated as %s" % approxintegral(200)
print "For N=1000, integral approximated as %s" % approxintegral()
print "For N=10000, integral approximated as %s" % approxintegral(10000)
print "For N=100000, integral approximated as %s" % approxintegral(100000)
print "For N=1000000, integral approximated as %s" % approxintegral(1000000)
print "For N=10000000, integral approximated as %s" % approxintegral(10000000)  # This seems to be the correct order of magnitude for 3 decimal places... 
