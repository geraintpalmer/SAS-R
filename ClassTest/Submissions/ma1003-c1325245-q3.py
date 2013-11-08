import random

class Integral():
    """     A class for the integral of a curve 1 - x^2
    Attributes:
        x: the x 
        y: the y coordinate of the point
        incircle: a boolean indicating whether or not the point is in the inscribed circled
        """    def __init__(self, r=1):
            self.x = (.5 - random.random()) * 2 * r
            self.y = (.5 - random.random()) * 2 * r
            self.incircle = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2  # This returns the boolean corresponding to whether or not the point is under the curev
            def approxpi(N=1000):
                """
                Function to return an approximation for pi using montecarlo simulation
                Arguments: N (default=1000) which is the number of points
                Outputs: An approximation of pi
                """
                numberofpointsincircle = 0
                for i in range(N):  # A loop to drop sufficient points
            drop = Drop()  # Generate a new drop
            if drop.incircle:  # Check if drop is in circle
                numberofpointsincircle += 1
        return 4 * numberofpointsincircle / float(N)     ######################################### # This is possibly pushing students a bit. Compares approximations to actual # value of pi using the 'math' library. bestapproxdif = abs(approxpi(1) - math.pi)  # Initiate a best approximation bestN = 1  # Corresponding N for N in range(2, 10001):  # Check approximation for 10000 values of N     approxdif = abs(approxpi(N) - math.pi)  # check how good new approximation is     if approxdif < bestapproxdif:  # if approximation is better update best values         bestapproxdix = approxdif         bestN = N print "Best N is: %s" % bestN # This indicates that increasing the number of points improves the # approximation (which is logical) #########################################   print "For N=200, pi approximated as %s" % approxpi(200) print "For N=1000, pi approximated as %s" % approxpi() print "For N=10000, pi approximated as %s" % approxpi(10000) print "For N=100000, pi approximated as %s" % approxpi(100000) print "For N=1000000, pi approximated as %s" % approxpi(1000000) print "For N=10000000, pi approximated as %s" % approxpi(10000000)  # This seems to be the correct order of magnitude for 3 decimal places... 

    
#not fininshed
