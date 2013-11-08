"""
Class test - question 3
C1330008
"""

import random

class Point():
    """
    A class for a point falling under a graph in a square

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        undergraph: a boolean indicating whether or not the point is under the graph and in the square
        """
    
    def __init__(self, r = 1):
        self.x = (.5 - random.random()) 
