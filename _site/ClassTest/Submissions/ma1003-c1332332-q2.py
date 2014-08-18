"""
Class test - question 2
c1332332
"""

import csv  # Importing this library as can also be used to import data

f = open("classtestdata.csv", "r")
csvdata = csv.reader(f)
data = [row for row in csvdata]  # Read all data in to a list
f.close()  # Close file

print len(data)

data = [[len(e) for e in row] for row in data]

