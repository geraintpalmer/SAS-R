'''
Class test - q3
c1325348
'''

import random # This imports random library
import math  # This imports math library

f(x) = 1 - x**2

class Point():
    '''
    A class for a point landing under the graph

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        undergraph: a boolean indicating whether or not the point is under the graph
    '''
    def__init__(self, r=1):
        self.x =
        self.y =
        self.undergraph = 1 - x ** 2 >= (r) # This returns the boolean whether or not the point is under the graph
        
def approx(N=1000):
    '''
    Function to return an approximation for the value of the integral

    Outputs: An approximation of the integral
    '''

    numberofpointsinsquare = 0
    for i in range(N): 
        point = Point() # Generates a new point
        if point.undergraph: # Check if drop is under graph
            numberofpointsinsquare += 1
