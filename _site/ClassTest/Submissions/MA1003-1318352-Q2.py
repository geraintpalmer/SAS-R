"""
Class test - question 2
C1318352
"""

import csv  # Importing the csv library as it can also be used to import data

f = open("classtestdata.csv", "r")
csvreader = csv.reader(f)  # Using the csv library to read the data in the csv
data = [row for row in csvreader]# Reading all the data into a list
f.close()

print "The number of names in the data file is %s." % (len(data))

dataformean = [len(row[0]) for row in data]  # Evaluates the length of each of the names in the data

def mean(n):
    """
    Creating a function which finds the mean of a list of numbers.

    Argument: A list of numbers

    Output: The mean of the list of numbers
    """
    return sum(n) / len(n)

print "The mean length of the names in the data file is %s." % mean(dataformean)
