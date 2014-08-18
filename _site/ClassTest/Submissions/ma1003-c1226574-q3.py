'''
Class test question 3
C1226574
'''

import random
class Point():
    def __init__(self, r=1):
        self.x = (.5 - random.random())  * r
        self.y = (.5 - random.random())  * r
        self.underline = (self.x) - 1/3 * (self.x) ** 3

n = 0
a = 1000
l = []
for n in range(0,a):
    pt = Point()
    print pt.underline
    l.append(p.underline)
y = 0
x =sum(e for e in l)/len(l)
print x
