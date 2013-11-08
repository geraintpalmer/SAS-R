"""
class test - question 3
c1320382
"""

import random  # Imports the random library

class Point():
    """
    A class for a random point in the square

    Attributes:
        x: the x co ordinate of the point
        y: the y co ordinate of the point
        undergraph: a boolean indicating whether or not the point is under the graph
    """
    def __init__(self, r=1):
        self.x = (random.random())
        self.y = (random.random())
        self.undergraph = (self.y) + (self.x) ** 2 <= 1  # Returns boolean corresponding to whether or not point is under graph

def approxval(N=1000):
    """
    Function to return an approximation for required integral using montecarlo simulation

    Arguments: N (default = 1000) which is the number of points

    Outputs: An approximation of the integral of 1 - x ** 2 between 0 and 1
    """
    numberofpoints = 0
    for i in range(N):  # A loop to generate enough points
        point = Point()  # Plots a random point
        if point.undergraph:  # Checks if point is under the graph
            numberofpoints += 1
    return numberofpoints / float(N)
