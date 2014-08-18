"""
Class test - question 2
c1324239
"""
import csv  # Imports the csv module

f = open('classtestdata.csv')
csvrdr = csv.reader(f)
data = [row for row in csvrdr]
f.close()

print "There are %i names in the file" % len(data)  # Prints how many names in total are in the file


def meanlengthofnames(row):
    for row in row in data:
        return len(row)
        

