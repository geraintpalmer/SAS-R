"""
Class test - question 2
C1370824
"""

import csv  # Am importing this library as can also be used to import data

f = open('classtestdata.csv', 'r')
csvdata = csv.reader(f)  # This is a slightly messier file to read manually so using the csv library
data = [row for row in csvdata]  # Read all data in to a list
f.close()  # Close file

data = [str(e) for e in data]  # Convert to string

#print data

l = []  # Making a list l
l = data  # Putting the data into the list l
print len(l)  # Printing the number of total names in the data file

average = sum(len(l) for l in l)/len(l)  #
print average  #Printing the average
