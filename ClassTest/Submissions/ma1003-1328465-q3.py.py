import random # imports the random library

class Area(): #creating a class
    """
    A class for the area under the graph

    x: the x coordinate of the point
    y: the y cooridnate of the point

    

    """
    def _init_(self,):
        self.x = (.5 - random.random()) * 1
        self.y = (.5 - random.random()) * 1
        self.undergraph = 1 - x ** 2 
