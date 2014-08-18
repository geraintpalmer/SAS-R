import random
import math

class Point(): #capital for a class

    """
    A class for the probability P of point landing under the graph

    attributes:
    x: the x coordinate
    y: the y coordinate
    undergraph: a boolean indicating hwether or not the point is under the graph
    """

def __init__(self, r=1):
    self.x (.5 - random.random()) * 2 * r
    self.y (.5 - random.random()) * 2 * r
    self.undergraph = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2
"""
this returns the boolean corresponding to whether the point is under the graph
"""

numberofpointsundergraph = 0
for i in range(N): # a loop to drop sufficient points
    point = Point() # generate a new point
    if point.undergraph: # check if poit is under graph
        numberofpointsundergraph += 1
    return 4 * numberofpointsundergraph / float(N)

