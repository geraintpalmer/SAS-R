"""
Class test- question 1
c1324557
"""

def parabola(x):
    y = 1 - x*x
    return y

def approx_area(fn, a, b, n):
    """
    Approximate the area under fn in the interval [a,b]
    by adding the area of n rectangular slices.
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

