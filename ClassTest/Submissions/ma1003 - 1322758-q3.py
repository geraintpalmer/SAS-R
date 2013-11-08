"""
Class test - question 3
c1322758
"""
import random  # imports the random library

class Area():
    """
    A class for area under a curve 1 - x^2
    Attributes :
    x : the x coordinate of the point
    y : the y coordinate of the point
    under whether the point lies under the curve
    """
    def __init__(self, r = 1):
        self.x = (0.5 - random.random()) * 2 * r
        self.y = (0.5 - random.random()) * 2 * r
        self.under = 1 - self.x ** 2 <= self.y  # this returns the boolean corresponding to whether the point lies under the curve

jack = Area()
print jack.under

def approxarea(N):
    """
Function to return approximated area under curve
Arguements : N
outputs : approximate area
"""
    pointsundercurve = 0
    for i in range(N):
        area = Area()
    if area.under:
        pointsundercurve += 1
    return pointsundercurve
    
print approxarea(100)
