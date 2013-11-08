import random # This imports a random selection of data

class Area():
    """
    A class for the probability of points being randomly drawn on the square.

    Attributes:
    x: the x coordinate of the point
    y: the y7 coordinate of the point
    insquare: a boolean indicating whether the point is in the square.
    """

    def __init__(self, r=1):
        self.x = (.5 - random.random()) - 1 * x ^ 2
        self.y = (.5 - random.random()) - 1 * x ^ 2
        self.insquare = (self.y) - (self.x) ** 2 <= (r)
    

def integral():
    """
    A function that allows us to find the area under the curve between 0 and 1.
    Arguments:
    Outputs: The area under the curve.
    """

    
