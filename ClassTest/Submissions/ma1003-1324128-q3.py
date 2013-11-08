"""
Class test - question 3
C1324128
"""

import random
import math  # This is not necessarily needed but will be useful for some comparisons later on.
 
 
class Point():
    """
    A class for a point landing under the graph
 
    Attributes:
        x: the x coordinate of the point
        undergraph: a boolean indicating whether or not the point is under the graph
    """
    def __init__(self):
        self.x = (random.random()) * 1
        self.undergraph = ((self.x) - ((self.x) ** 3)/3 <= 1, 0, 1)  # This returns the boolean corresponding to whether or not the point is under the graph
 
point = Point()
print point
print point.x
