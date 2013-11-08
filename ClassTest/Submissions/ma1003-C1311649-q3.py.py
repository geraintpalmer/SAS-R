"""
Class Test - Question 3
C1311649
"""

import random
import math  
 
 
class Land():
      def __init__(self, r=1):
        self.x = random.random()
        self.curve = [(1 - (random.random() ** 2)), 0, 1]
        self.undercurve = self.curve <= (r)  # This returns the boolean corresponding to whether or not the point is in the circle
 
 
def approxarea(N=1000):
    """
    Function to return an approximation for the area under the curve
 
    Arguments: N (default=1000) which is the number of points
 
    Outputs: An approximation of the area under the curve
    """
    numberofpointsundercurve = 0
    for i in range(N):  # A loop to drop sufficient points
        land = Land()  # Generate a new drop
        if land.undercurve:  # Check if drop is undercurve
            numberofpointsundercurve += 1
    return numberofpointsiundercurve

print approxarea(N=1000)
