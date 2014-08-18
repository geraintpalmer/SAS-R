"""
Class test - question 2
c1312192
"""

import csv
f = open("classtestdata.csv", 'r') 
csvrdr = csv.reader(f) # Using csv library
data = [row for row in csvrdr] #read data into a list
f.close() #Close file
data = [[float(e) for e in row] for row in data[0:]]

listofnames = [] # Initialise empty list

print len(data)

