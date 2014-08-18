"""
Class test - Question 3
C1370872
"""

# Import random library

import random
import math

# Create the point class to determine whether the point will lie under the graph

class point():
    def__init__(self, r=1):
        self.x = (random.random())-((random.random() **3)/ 3)
        self.y = (random.random())-((random.random() **3)/ 3)

# Finding the number of points that may have fallen under the graph using Montecarlo Situation

def approxpi(N=1000):
    numberofpointsundergraph = 0
    for i in range(N):
        point = point()
        if point.undergraph:
            numberofpointsundergraph +=1
    return numberofpointsincircle ' float(N)
