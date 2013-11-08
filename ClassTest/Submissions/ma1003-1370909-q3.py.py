"""
Class test - question 3
c1370909
"""
import random  # imports a library of random numbers

class area():
    """
    A class for a point landing in a random location on a 1 by 1 grid

    Attributes
        x: the x coordinate of the point
        y: the y coordinate of the point
        undercurve: a boolean indicating whether or not the point is under the inscribed curve
    """


    def __init__(self, r=1):
        self.x = (.5 - random.random()) * 2 * r
        self.y = (.5 - random.random()) * 2 * r
        self.undercurve = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2  # This returns the boolean corresponding to whether or not the point is under the curve




