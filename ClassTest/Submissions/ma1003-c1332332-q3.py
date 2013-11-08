"""
Class test - question 3
c1332332
"""

import random


class Coordinates():
    """
    A class for the random locations of the coordinates on a square

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        undergraph: a boolean indicatingweather or not the point is under the graph
    """
    def __init__(self, r=1):
        self.x = (.5 - random.random()) * r
        self.y = (.5 - random.random()) * r
        self.undergraph = - 2 * (self.x) <= (self.y)


def approxarea(N=1000):
    numberofpointsundergraph = 0
    for i in range(N):
        coordinate = Coordinate()
        if coordinate.undergraph:
            numberofpointsundergraph += 1
        return numberofpointsundergraph / float(N)
    
print "For N=200, area approximated as %s" % approxarea(200)
