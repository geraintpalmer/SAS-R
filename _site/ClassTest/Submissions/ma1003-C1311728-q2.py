"""
Class test - question 2
C1311728
"""

import csv # Imports csv file

f = open('classtestdata.csv', 'r') # Imports csv file
csvrdr = csv.reader(f)
data = [row for row in csvrdr]
f.close() # Closes csv file


data = [[str(k) for k in row] for row in data[0:]] # Converts data to a string for each element of the data
print data # Prints the data

print len(data)  # Prints the length of the data

word = str(k)
print word


