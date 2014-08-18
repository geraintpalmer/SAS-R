"""
Class test - question 3
c1307787
"""

import random

class Coord():
    """
    A class for a random coordinate landing under graph

    Attributes:
        x: x coordinate of the point
        Y: y coordinate of the point
        undergraph: a boolean indicating whether or not the point is below the graph
   """
def __init__(self, r = 1):
    self.x = (.5 - random.random()) * r
    self.y = (.5 - random.random()) * r
    self.undergraph = (self.x) + (self.y) <= 1 - (r ** 2) # This returns the boolean corresponding to whether the point is under the graph or not

def approx(N = 1000):
    """
    Function to return an approximation for the integral 1 - x between 0 and 1

    Arguments: N which is number of points

    Outputs: Approximation to the integral
    """
    munundergraph = 0
    for i in range(N): # A loop top drop enough points
        point = Coord() # Generate a new point
        if point.undergraph: # Check if the point is under the graph
            numundergraph += 1
    return numundergraph / float(N)

print approx(200)
    
