import random  # Imports the "random" module

class Points():
    """
    A class for a point being put in a random location on a square

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        undergraph: a boolean indicating whether or no the point is under the drawn graph
    """
    def __init__(self, r=0.5):
        self.x = (.25 - random.random()) * 2 * r
        self.y = (.25 - random.random()) * 2 * r
        self.undergraph =(self.y) - 1 + (self.x) ** 2 <= 0  # This shows whether or not the point is under the graph or not using boolean


def approxareaundergraph(N = 1000):
    """
    A function to return an approximation of the area under the graph

    Arguments: N, the number of points

    Outputs: An apporximation of the area under the graph (Intergral of 1 - x ** 2)
    """
    numberofpointsundergraph = 0
    for i in range(N):  # This loop will plot the points
        point = Points()  # Generate new point
        if point.undergraph:  # If the point is under the graph
            numberofpointsundergraph += 1  # Add 1 to the number of points
    return numberofpointsundergraph

