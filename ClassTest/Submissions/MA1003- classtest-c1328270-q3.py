import random  # Import the random library


class Points():
    """
    A class for a points of random coordinates in this square

    Attributes:
        x: the x coordinate of the point
        y: the y coordinates of the point
        undergraph: a boolean indicating whether or not the point is under the graph
    """
    def __init__(self, r = 1):
        self.x = (1 - random.random()) * 1 * r
        self.y = (random.random()) * 1 * r
        self.undergraph = 1 / 3 * (self.x) ** 3  # This returns the boolean corresponding to whether or not the point is under the graph


def approxpoint(N = 100):
    """
    Function to return an approximation for P

    Arguments: N (default = 100) which is the number of points

    Outputs: An aproximation of P
    """
    numberofpointsundergraph = 0
    for i in range(N):  # A loop for sufficient points
        point = Points()  # Generate a new point
        if point.undergraph:  # Check if the point is under the graph
            numberofpointsundergraph += 1
    return numberofpointsundergraph / float(N)


point = [Points() for k in range(20000)]

print 4 * len([d for d in point if d. numberofpointsundergraph]) / float(len(point))
        
