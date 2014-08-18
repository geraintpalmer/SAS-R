"""
Class Test - Question 2
C1318789
"""


textfile = open('classtestdata.csv', 'r')    #opens the data in 'read mode'
string = textfile.read()

data = string.split('\n')  # separates the names to change string into a list
list = data

a = len(data)  # adds up the number of elements in 'data' (number of names within list)
print "Total number of names in Class Test Data:"
print a

b = len(string)  # adds up the number of characters within the string

c = b/a  # divides number of characters by number of elements to give a value for the mean
print "Mean length of names in Class Test Data:"
print c





