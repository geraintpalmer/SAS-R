"""
Class test - Question 3
C1311689
"""

import random   

class Points():
    """
    A class for a coordinate being placed at a random point in a square

    Attribute:
    x: The x coordinate of the point
    y: The y coordinate of the point
    undercurve: a boolean indicating whether or not the point is under the curve
    """

    def __init__(self, r=.5):
        self.x = (.5 - random.random()) * 2 * r
        self.y = (.5 - random.random()) * 2 * r
        self.undercurve = 1 - (self.x) ** 2 <= 0  #This returns a boolean corresponding to whether or not the point is under the curve

def approxvalue(N= ):
    """
    Function to return an approximation for the area under the curve

    Arguments: N (number of points placed)

    Outputs: an approximation of the area under the curve
    """

    numberofpointsundercurve = 0
    for i in range(N):    #A loop to place sufficient points
        point = Points()   #Generates a new point
        if point.undercurve:   #Checks if point is under curve
            numberofpointsundercurve +=1
    return
