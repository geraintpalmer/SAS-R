"""
Class test - question 2
C1325939
"""

import csv #  Am importing this library as can also be used to import data

f = open('classtestdata.csv', 'r')
csvdata = csv.reader(f)  # This is a slightly messier file to read manually so using the csv library
data = [row for row in csvdata]  # Read all data in to a list
f.close()  # Close file


print len(data) #  Prints to screen how many total names are in the data file

l = [for every row in data] #  For every individual name
print mean len(l) #  Prints to screen the mean length of names in the file
