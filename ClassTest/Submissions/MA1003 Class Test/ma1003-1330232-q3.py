"""
Class test - question 3
C1330232
"""

import random  # importing the random library
import math

class Drop():  # our class to help us approximate the value of our integral
    def __init__(self, a, b):
        self.a = 0
        self.b = 1
        self.undergraph = integral( 1 - x ^ 2, self.a, self.b,dx)


        
def approx(N=1000):
"""
a function to calculate the approximate area under graph therefore our integral

Arguments: numner of points N

Output: area under graphn
"""
    areaundergraph = 0
    for i in range(N):
        drop = Drop()
        if drop.undergraph:
            areaundergraph += 1
    return areaundergraph

print approx(N=10000)
