#define a function f(x) = 1 - x^2#

def func():
    y = 1 - x ** 2
    """
    arguemnts : y = 1 - x ** 2
    outputs : the integral value of y
    """
    
#we want to integrate y#

#lets try using classes to help us#

class Drop():
    def __init__(self, r=1):
        self.x = (.5 - random.random()) * 1
        self.y = (.5 - random.random()) * 1
        self.insquare = (self.y) * (self.x)
        
