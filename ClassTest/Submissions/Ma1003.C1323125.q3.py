import random  # import the random library
 
class Point():

"""
create a class for a random point in the square
attributes : x = x co-ordinate
             y = y co-ordinate
             self.underline = tells you if the point is under the line 1 - x^2
""""
    def __init__(self, x=1):
        self.x = (1 - random.random())  # Choosing a random x co-ordinate
        self.y = (1 - random.random())  # Choosing a random y co-ordinate
        self.underline = 1 - self.x ** 2

def approxint(N= 1000):

"""
A function to return an approximate value of the integral
Argument: N = the number of points
Output: approximation of the integral
"""
    pointsunderline = 0
    for i in range(N)
    point = Point()
    if point.underline:
        pointsunderline += 1
    return len(pointsunderline)/n

