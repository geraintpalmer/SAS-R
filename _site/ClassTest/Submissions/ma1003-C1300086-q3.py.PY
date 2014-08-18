"""
 Class test - Question 3
 c1300086
"""


import random
import math

class Point():
    def __init__(self, r=1):
        self.x = (random.random())  #give x random value between 0 and 1
        self.y= (random.random()) # give y random value between 0 and 1
        self.belowgraph = (self.y) <= 1 - (self.x)**2  # if y less then 1-x**2 then assign below graph

def approxarea(N):

    numberofpointsundercurve = 0
    for i in range(N):
        point = Point()
        if point.belowgraph:   # check if point below graph
            numberofpointsundercurve += 1 # add one to number points under circle
    return numberofpointsundercurve/ float(N)

print approxarea(10)
