"""
Class Test - Question 2
C1326700
"""



import csv  # Am importing this library as can also be used to import data

f = open('classtest.csv', 'r')
csvdata = csv.reader(f)  # This is a slightly messier file to read manually so using the csv library
data = [row for row in csvdata]  # Read all data in to a list
f.close()  # Close file

print len(data) #print the length of the data, i.e number of names

print len([e for e in set(data)])  # Uses the set command to remove duplicates from data, leaving us with only unique names

