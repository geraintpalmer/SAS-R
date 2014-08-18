"""
Class test - question 3
C1312104
"""

"""
integral of 1 - x ^ 2 is x - (x ^ 3) / 3
given we are integrating between 0 and 1, the area becomes 2/3,
thus so is the probability
"""


class Drop():
    def __init__(self, r=1):
        self.x = (.5 - random.random()) * 2 * r
        self.y = (.5 - random.random()) * 2 * r
        self.incircle = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2

def parabola(x):
    """
    This function is to create my parabola
    y is  a dummy variable to describe the function, and distance up the side of the box
    x is another dummy variable to describe the function and the distance along the box#
    the output is a curve remarkably similar to a parabola going through (0, 1) and (1, 0)
    """
    y = 1 - x*x  # describes my function
    return y  # sets parabola(x) to my function

def approx_area(fn, a, b, n):
    """
    Approximate the area under fn in the interval [a,b]
    by adding the area of n rectangular slices.
    a, b, n are integers that describe the boxes the area is to be split up into
    area is the area under my function
    output is the area below my function in a certain range
    """

    a = float(a)
    b = float(b)
    area = 0.0
    for slice in range(n):
        left = a + (b-a)*slice/n
        right = a + (b-a)*(slice+1)/n
        mid = (left + right)*0.5
        height = fn(mid)
        width = right - left
        area += height * width

    return area

print "Area is", approx_area(parabola, 0, 1.0, 5000)  # This area is now the area under the curve in our box, i have chosen 5000 so as to be suitably accurate

import random
r = random.randint(1001, 10000)

"""
The idea is to now aproximate the area using "drops"
