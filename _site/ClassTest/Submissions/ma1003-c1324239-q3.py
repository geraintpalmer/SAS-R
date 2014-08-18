"""
Class test - question 3
c1324239
"""
import random
 
class Point():
    """
    A class for a point falling in a random location in the square
 
    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        incircle: a boolean indicating whether or not the point is in the inscribed curve
    """
    def __init__(self, x):
        self.x = (random.random())
        self.undercurve = 2 * self.x <= 1  # This returns the boolean corresponding to whether or not the point is in the circle
 
 
def approxarea(N):
    """
    Function to return an approximation for pi using montecarlo simulation
 
    Arguments: N (default=1000) which is the number of points
 
    Outputs: An approximation of the area under the curve
    """
    numberofpointsundercurve = 0
    for i in range(N):  # A loop to drop sufficient points
        point = Point()  # Generate a new point
        if point.undercurve:  # Check if point is below the curve
            numberofpointsundercurve += 1
    return 2 * numberofpointsundercurve

