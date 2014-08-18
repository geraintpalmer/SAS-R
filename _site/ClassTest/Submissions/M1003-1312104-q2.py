"""
Class test - question 2
C1312104
"""

"""
A series of commands to return:
    a) number of names in the file
    b) the mean length of the names
    c) the number of unique names  in the file

Arguments:
f is a dummy variable for the file of data
data is the actuall data retrieved from the file
n is a list of the lenght of names (integers)
mean is a specific integer, being that of the mean of the names

Outputs 3 numbers:
    1) the number of names
    2) the mean length
    3) the number of unique names
"""
f = open('classtestdata.csv', 'r')  # These 3 lines are to open the file, read it and then close said file
data = f.read()
f.close()

data = data.split('\n')  # This is to create a list of the data that was in the file

print len(data)  # The program then prints how many names my data has in it

n = []  # Here I create a set to contain the length of all the names in data 
for row in data:  # for loop to add to my n the length of all names
    n.append(len(row))
mean = sum(n)/len(data)  # finding the mean of the length of the names and then printing it
print mean  # Prints the mean length of the names in data

mydata = set(data)  # set function that takes 1 of each unique name and creates a new list containing only 1 of each name from data
print len(mydata)  # It is now simple to print the length of this list, giving the number of unique names
