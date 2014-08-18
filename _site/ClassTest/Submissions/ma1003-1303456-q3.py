"""
Class test - question 2
c1303456
"""


import random  # Imports the random library


class Coordinate():
    """
    A class for a point at random coordinates in the square
    Attributes:
        x: the x coordinate
        y: the y coordinate
        undercurve: a boolean indicating whether or not the point is under the curve
    """
    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        self.undercurve = 1 - x ** 2
        
def approx(N=1000):
    count = 0
 
        
