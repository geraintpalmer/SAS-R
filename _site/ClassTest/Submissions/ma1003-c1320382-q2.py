"""
class test - question 2
c1320382
"""
import csv  # Am importing this library as can also be used to import data 

f = open("classtestdata.csv", 'r')
csvdata = csv.reader(f)
data = [row for row in csvdata]  # Read data into a list
f.close()  # Close file

totalnames = len([e for e in data])  # Counts the number of elements
print "The total number of names in the file is %i" % (totalnames)  # Prints number of elements

class Name():
    """
    A class for the names

    Attributes:
        name: the string containting the name
        namelength: an integer, the length of each name
    """
    def __init__ (self, name, namelength):
        self.namelength = namelength
        self.name = name

totallength = 0
for element in data:
    name = element[0:10]
    namelength = len(name)
    totallength += namelength

print totallength
