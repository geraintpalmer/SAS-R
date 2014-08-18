"""
Class test - question 2
c1308412
"""

import random  # Imports a random library

class Point():
    """
    A class for a random point on the grid

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        undergraph: a boolean indicating whether or not the point is under the described graph
    """
    def __init__(self):
        self.x = random.random(0,1)
        self.y = random.random(0,1)
        self.undergraph = (self.y) <= 1  - (self.x) ** 2  # Returns a boolean as to whether or not the point is under the graph

def approxarea(N=1000):
    """
    Function to return the approximate area under the graph

    Arguements: N (default=1000) which is the number of points

    Outputs: An approximation of the area
    """
    numberofpointsundergraph = 0
    for i in range(N):
        point = Point()  # Adds a point to the class
        if point.undergraph:
            numberofpointsundergraph += 1
    print numberofpointsundergraph / float(N)

