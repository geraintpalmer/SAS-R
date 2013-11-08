import random  #imports the random library

class Graph():  #creates a new class
    def __init__(self, r = 1):  #definies a function within the class with variables self, x, y and set defult values to 1 because the suare with the graph in is 1 units squared in size
        self.x= (random.random()) * 2 * r
       
        self.areaundergraph = 1 - (self.x - (self.x **3)/3)#the integrated function of f(x)

def approxintegral(N = 1):
    area_undergraph = 0  #variable assigned to zero = COUNTER??
    for i in range(N):  #a loop to drop sufficient points
        graph = Graph()  #generate a new graph
        if graph.areaundergraph: #check if the graph is in the boc
            area_undergraph +=1  #i is added if the thing is in the box
    return areaundergraph / float (N) #divides area under graph by areain the box

print "for N = 1, the area under the graph is approximated as %s" %approxintegral(70)        
    
