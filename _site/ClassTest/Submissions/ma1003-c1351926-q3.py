
"""

class test - question 3
c1351926
"""
x = 0
import random
class Drop():
    def __init__(self, r=1):
        self.x = (.5 - random.random()) - (x ** 3)/3
        self.y = (.5 - random.random()) * 2 * r
        self.incircle = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2

for i in range(10):
        triali = Drop(r = i)
        print "x%i:" % i, triali.x
        print "y%i" % i,triali.y
        print triali.incircle
