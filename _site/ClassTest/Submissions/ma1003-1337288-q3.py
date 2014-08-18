import random #Import the random library.

class Point():
	"""
	Creates a class for a random point within a square of area 1.
	
	Attributes:
		self.x : The x coordinate of the point.
		self.y : The y coordinate of the point.
		self.undercurve : Boolean of whether or not the point is under the curve.
	"""
	def __init__(self):
		self.x = random.random()
		self.y = random.random()
		self.undercurve = (self.y) <= 1 - (self.x) ** 2
		
def approxarea(n):		#Function to approximate the area under the curve.
	numberunder = 0
	for i in range(n+1):
		point = Point()
		if point.undercurve:
			numberunder += 1
	return numberunder / float(n)
	
print "For n=100, area is approximated as %s." % approxarea(100)		#Multiple approximations for different values of n.
print "For n=200, area is approximated as %s." % approxarea(200) 
print "For n=500, area is approximated as %s." % approxarea(500) 
print "For n=1000, area is approximated as %s." % approxarea(1000)
print "For n=2000, area is approximated as %s." % approxarea(2000)
print "For n=5000, area is approximated as %s." % approxarea(5000)
print "For n=10000, area is approximated as %s." % approxarea(10000)
print "For n=100000, area is approximated as %s." % approxarea(100000)