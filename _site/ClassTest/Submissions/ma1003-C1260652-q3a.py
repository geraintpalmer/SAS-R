"""
Class Test - Question 3
C1260652
"""

import random  # Importing the random library

class Point():
    """
    A Class for a point landing landing under the graph

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        undergraph: a boolean indicating whether or not the point is under the graph
    """
    def __init__(self, x, y):
        self.lengthofgrid = x 
        self.widthofgrid = y
        self.undergraph = (self.y) ** 2 -(self.x) ** 2 <= (r) ** 2  # Returns the boolean corresponding to whether or not the point is under the graph

