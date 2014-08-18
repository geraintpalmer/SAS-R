import random

class Point():
    """
    A class for a random point int he square
    Attributes:
    x : the x coord
    y: the y coord
    insquare: boolean indicating whether or not the point is in the square
    """

    def __init__(self, d=1)
    self.x = (.5 = random.random()) * d)
    self.y = (.5 = random.random()) * d)
    self.insquare = (self.x) ** 2 + (self.y) ** 2 <= d

def approxarea(N=1000):
    """
    A function to return an approximation for the area under a graph
    Arguments: N (default = 1000) which is number of points
    Outputs: An approximation of the area under the graph 1-x^2 between 0 and 1
    """
    numberofpointsinsquare = 0
    for i in range(N):
        point = Point
        if point.insquare:
            numberofpointsinsquare += 1
    return 4* numberofpointsinsquare / float(N)

bestapprox
