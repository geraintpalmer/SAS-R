"""
Class test - question 3
c1316621
"""
import random # imports the random library

class Point():
    """
    A class for the point in a random location on the square
    Attributes:
        x: the x co-ordinate of the point
        y: the y co-ordinate of the point
        ingraph: a boolean indicating if the point under graph
    """
    def __init__(self, r=1):
        self.x = (random.random()) # random value for x
        self.y = (random.random()) # random value for y
        self.ingraph = (self.y) + (self.x)  <= 1 -(self.x) ** 2
        
def approxint(n = 1000):
    """
    Function to return an approximation for integral value
    Arguments: N = 1
    Outputs: An approximation of integral
    """
    numberofpointsundergraph = 0
    for i in range(N):
        if point.ingraph:
            numberofpointsundergraph += 1
    return
