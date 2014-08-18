"""
class test question 3
"""

class Drop():
    def __init__(self, r=1):
        self.x = (.5 - random.random()) * 2 * r
        self.y = (.5 - random.random()) * 2 * r
        self.incircle = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2

For i in range (10) :
    
