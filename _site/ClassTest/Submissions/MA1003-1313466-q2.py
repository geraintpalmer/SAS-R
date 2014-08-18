"""
Class test - question 2
C1313466
"""

import csv  # Am importing this library as can also be used to import data 

f = open('classtestdata1.csv', 'r')
csvdata = csv.reader(f)  # This is a slightly messier file to read manually so using the csv library 
data = [row for row in csvdata]  # Read all data in to a list 
f.close()
data = [[float(e) for e in row] for row in data[1:]]  # Convert relevant data to float 

data = string.split('\n')  #'\n' means data will be on the enxt line from this point onwards
print data

listofnames = []  #Initialise empty list
for row in data:
    listofnames.append(Name())



