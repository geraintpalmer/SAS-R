"""
Class test - question 3
c1339313
"""
x = 0
y = 0
import random


class Point():
    def __init__(self):
        self.x = (0.5 - random.random()) * 2
        self.y = (0.5 - random.random()) * 2
        self.inarea = 1 - (self.x) ** 2 <= self.y
n = 0
i = 1
while i < 10000:    
    q = Point()
    if q.inarea == True:
        n += 1
    i += 1
print float(n) / 10000
