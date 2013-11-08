"""
Class test - question 3
c1300859
"""
import random

class Drop():
    """
    A class for a rain drop falling in a random location on a square

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
            """
    def __init__(self):
        self.x = (random.random())
        self.y = (random.random())
          


def approx(N):
    """
    Function to return an approximation for integral

    Arguments: N which is the number of points

    Outputs: An approximation of the integral
    """
    numberofpoints = 0
    for i in range(N):  # A loop to drop sufficient points
        drop = Drop()  # Generate a new drop
        if drop(self.y) <= 1 - drop(x) ** 2:  # Check if drop is in under graph
            numberofpoints += 1
    return numberofpoints / 1
print approx(100000)
