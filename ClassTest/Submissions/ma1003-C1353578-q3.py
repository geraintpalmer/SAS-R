"""
class test question 3
c1353578
"""

import random

class Points():
    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        self.inarea = (self.y) <= 1 - (self.x) ** 2


def approxarea(N=1000):
    numberinside = 0
    for i in range(N):
        point = Points()
        if point.inarea:
            numberinside += 1
    return numberinside / float(N)
