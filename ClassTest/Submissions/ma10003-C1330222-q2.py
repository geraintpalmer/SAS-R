"""
Class test - question 2
C1330222
"""

import csv # Am importing this library as it can be used to import data


f = open('classtestdata.csv', 'r') # Opens file in read mode
csvobject = csv.reader(f) #Creates a csv reader object
data = [str(row[0]) for row in csvobject] #Converts the csv reaser object to data
f.close()

Totalnames = len([e for e in data]) # Prints total names in data file

print Totalnames



