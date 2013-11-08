"""
Class test - question 2
C1302175
"""

import csv

f = open('classtestdata.csv', 'r')  #Opens this file in read mode
csvrdr = csv.reader(f)  #Creates a csv reader object
data = [row for row in csvrdr]  #Converts the csv reader object into data
f.close()  #Closes the file

print len(data)  #This prints how many total names are in the data file



