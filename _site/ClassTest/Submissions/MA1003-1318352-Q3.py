"""
Class test - question 3
C1318352
"""

import random

class Point():
    """
    A class for creating random points in a square.

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        area: whether or not the point is in the required area
    """
    def __init__(self, r=1):
        self.x = (.5 - random.random()) * r
        self.y = (.5 - random.random()) * r
        self.area = (self.x) * (self.y) <= 1 - (self.x) ** 2

def approxvalue(N=1000):
    numberofpointsinarea = 0
    for i in range(N):
        point = Point()
        if point.area:
            numberofpointsinarea += 1
    return numberofpointsinarea

print approxvalue()
