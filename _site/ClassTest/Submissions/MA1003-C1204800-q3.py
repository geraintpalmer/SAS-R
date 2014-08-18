"""
Class test - question 3
C1204800
"""
 
import random
import math  # This is not necessarily needed but will be useful for some comparisons later on.
 
 
class Graph():
    """
    A class for a random point landing under the graph
 
    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        undergraph: a boolean indicating whether or not the point is under the graph
"""
    
    def __init__(self, r=1):
        for self.x[0,1], self.y[0,1]:
            self.x = (.5 - random.random()) * 1
            self.y = (.5 - random.random()) * 1
            self.undergraph = 1 - (self.x) ** 2 <= (self.y)  # This returns the boolean corresponding to whether or not the point is under the graph
 
 
numberofpointsundergraph = 0
for i in range(1000):  # A loop to drop sufficient points
    graph = Graph()  # Generate a new drop
    if graph.undergraph:  # Check if drop is in circle
        numberofpointsundergraph += 1
    else:
        return "False"
print numberofpointsundergraph

""
