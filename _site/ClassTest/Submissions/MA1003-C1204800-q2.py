"""
Class test - question 2
C1204800
"""

import csv

f = open('classtestdata.csv', 'r')  # open given data file
csvrdr = csv.reader(f)
data = [row for row in csvrdr]
f.close()

print data  # print a list of the names in the file

print len(data)  # print the number of rows in the data i.e. the number of names

for row in data:
    print len(row)

    



