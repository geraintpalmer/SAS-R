import random

class Point():
    """
    A class for a point P falling on a random location on the square

    Attributes:
        An x coordinate of the point
        A y coordinate of the point
        undercurve: a boolean indicating whether or not the point is under the curve
        """

    def __init__(self, p=1):
        self.x = (1 - random.random())  # Sets the x point as 1 - a random variable
        self.y = (1 - random.random())  # Sets the y point as 1 - a random variable
        self.undercurve = self.x * self.y <= (1 - (self.x) ** 2)  # Returns a boolean if the coordinates of the two are under the curve 1 - x ** 2
            
