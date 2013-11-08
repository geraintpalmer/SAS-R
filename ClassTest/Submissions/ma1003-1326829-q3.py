import random

class RandPoint():
    """
    A class for a random point on a graph

    Attributes:
        x: the x  coordinate
        y: the y coordinate
        belowgraph: a boolean indicating whether the point is below the curve y = 1-x^2
    """
    def __init__(self):

        self.x = random.random()
        self.y = random.random()
        self.belowgraph = self.y <= 1 - self.x**2

def approxfx(n):
    """
    Funnction to return an approximation of the area under curve 1 - x^2
    Inputs: n which is the number of points
    Outputs: an approximation for the area
    """
    pointsbelowgraph = 0    #Initialises points below greaph to zero
    for i in range(n):      #For loop saying repeat code in the loop n times
        point = RandPoint() # Creates an instance of the class RandPoint()
        if point.belowgraph:      #Checks if the point is below the graph
            pointsbelowgraph += 1 #if so increment by 1
    print n
    print pointsbelowgraph
    return pointsbelowgraph/n

print approxfx(1000)


