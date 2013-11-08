import random
import math

class Drop():
    """
    Drop is the probability of a point landing under the curve 1- x^2

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        undercurve: a boolean indicating whether or not the point is a point under the curve
    """
    def _init_(self, r = 1):
        self.x = (1 - random.random()) * 2 * r
        self.y = (1 - random.random()) * 2 * r
        self.undercurve = int(1 - (self.x) ** 2)

print Drop()
