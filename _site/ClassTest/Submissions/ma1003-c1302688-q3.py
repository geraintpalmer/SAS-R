import random
import math  # This is not necessarily needed but will be useful for some comparisons later on.

class Point ():
    """
    A class for a point landing in a random location in a square

    Attributes:
        x: the x co-ordinate of the point
        y: the y coordinate of the point
        undergraph: a boolean indicating whether or not the point is under the inscribed curve 1 - x ** 2.
    """
    def _init_(self, r = 1):
        self.x = (.5 - random.random()) * 2 * r
        self.y = (.5 - random.random()) * 2 * r
        self.undergraph = self.y + self.x <= 1 - x ** 2
        
def approxpi(N = 1000)
    """
    Function to return an approximation for pi using montecarlo simulation

    Arguments: N (default=1000) which is the number of points

    Outputs: An approximation of pi
    """
