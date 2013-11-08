"""
Class test - question 2
c1303456
"""


import csv  # Importing this library to allow csv data to be imported 
f = open("classtestdata.csv", "r")  # This opens the file which is being read
csvrdr = csv.reader(f)  # The csv library is being used to read the file
data = [row for row in csvrdr]  # This reads all data into a list
f.close()  # Closes file

length = len(data)  # defines length as the number of names in the list
print "There are %s names in the data file" % length  # Prints the number of names
mean = len(row) / length
print mean
