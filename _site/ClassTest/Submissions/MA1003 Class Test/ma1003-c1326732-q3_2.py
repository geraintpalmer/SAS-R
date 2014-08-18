"""Calculations suggest the integral should approximate to 2/3"""

import random  #Needed to make the drops randomize.
import math  
 
 
class Drop():
    """
    A class for a rain drop falling in a random location on a square
 
    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        incurve: a boolean indicating whether or not the point is in the inscribed curve
    """
    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        self.incurve = (self.y) <= 1 - ((self.x) ** 2)


def approximateintegral(N=1000):
    """ This approximates the area under the curve by creating N instances of drops and seeing if they are in the circle
    It creates a tally of all the drops that do go under the curve and a tally of all those that don't. It doesn't work though, I can't work out why!!"""
    inlist = 0
    outlist = 0
    for i in range(0, N):
        drop = Drop()
        if drop.incurve:
            inlist += 1
        else:
            outlist +=1

    print inlist / N
        

        
approximateintegral(1000)  #Testing with 1000 instances of drops, doesn't work, always comes out with 0...
