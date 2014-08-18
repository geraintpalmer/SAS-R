import random  #Import random library
import math

class Point():

    #Create a class for the probability of point P landing under the graph
    #Attributes: x is the upper limit, y is the lower limit of the integral
    #inintegral: a boolean indicating whether or not the point is in the inscribed circle
    
    def __init__(self, r=0):
        self.x = (1 - random.random()) + 1 - x * 2
        self.y = (0 - random.random()) + 1 - x * 2
        self.inintegral = 1 - (self.x) ** 2 - 1 - (self.y) ** 2  #Returns boolean corresponding to whether point is under the curve
        
