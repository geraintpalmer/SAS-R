"""
Class test - question 2
c1338218
"""

import csv

textfile = open('classtestdata.csv', 'r') # Opens a file in read mode
csvobject = csv.reader(textfile)  # Creates a csv reader object 
data = [str(row[0]) for row in csvobject]  # Converts the csv reader object to data
textfile.close()

print data

print len(data)

