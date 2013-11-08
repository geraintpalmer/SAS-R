import random

class Area():
    """
    A class to approximate the area under the curve, bound between a and b, using the trapezium rule

    Attributes:
        a: the lower x value which the curve is bound from
        b: the higher x value which the curve is bound up to
    """
    def approxarea(f, a, b):
        return (b - a) * ((f(a) + f(b)) / 2)  # this creates an approximation to the area under the curve f bounded by a and b
    
f(x) = 1 - x ** 2  # this is the function we wish to integrate

print approxarea(f(x), 0 ,1)

