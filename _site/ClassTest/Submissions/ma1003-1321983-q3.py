"""
solution to question 3 in class test
"""

import random
import math # not nexessarily needed but may be helpful

class point ():
    """
the probability P of a point landing under the graph
attributes
f(x): 1 - x ** 2
grid has area 1

"""
    def _init_(self, r=1):
        self.x = (.5- random.random())
        self.undergraph = 1 - (self.x) ** 2


def approxpoint(N=1):
    """
    Function to return an approximation 

    Arguments: N (default=1) which is the number of points

    Outputs: An approximation to the number of points
    """
    numberofpointsincircle = 0
    for i in range(N):  # A loop to sufficient points
        point = Point()  # Generate a new point
        if point.undergraph:  # Check if point is undergraph
            numberofpointsundergraph += 1
    return numberofpointsundergraph / float(N)




print "For N=0.1, points approximated as %s" % approxpi(0.1)
print "For N=0.2, points approximated as %s" % approxpi(0.2)
print "For N=0.3, points approximated as %s" % approxpi(0.3)
print "For N=0.4, points approximated as %s" % approxpi(0.4)
print "For N=0.5, points approximated as %s" % approxpi(0.5)
print "For N=0.6, points approximated as %s" % approxpi(0.6)  
