"""
Class test - question 2
c1316800
"""
import csv  # am importing library as can be used to import data

f = open('classtestdata.csv', 'r')  # opening the file
csvdata = csv.reader(f) # reading file using csv library
data = [row for row in csvdata]  # read all data into a list
f.close

print f  # prints the instance of the file

