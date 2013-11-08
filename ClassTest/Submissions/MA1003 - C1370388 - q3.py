"""
Class test - question 3
C1370388
"""

import random # imports the random library

class Point():
    """
    creates a class for a random point falling underneath the graph
    x is the x coordinate of the point, y is the y coordinate of the point
    undergraph = boolean indicating whether the point is under the graph or not
"""
    
    def __init__(self, r = 1):

        """
method that can be run when an instance is created
allows us to pass arguments to an instance of class when it is initialised to set attributes
i.e. the attributes of x and y set out above
"""

        self.x = (.5 - random.random()) * 2 * r
        self.y = (.5 - random.random()) * 2 * r
        self.undergraph = 1 - (self.x) ** 2 <= r # whether or not the point is under the graph

def approxval(N=1000): # chosen 1000 instances to gain a reliable probability, more repetitions
    numberofpointsundergraph = 0 # initial number of points under graph
    for i in range(N): # loop to drop points
        point = Point() # generates a new point under the graph
        if point.undergraph:
            numberofpointsundergraph += 1
        """
check to see if the point is under the graph, if it is,
then add one more point to numberofpointsundergraph, which
counts cumulatively how many points there are

"""

    return numberofpointsundergraph # prints how many points out of 1000 were under the graph
