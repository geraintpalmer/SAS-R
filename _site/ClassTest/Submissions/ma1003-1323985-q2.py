"""
Class test - question 2
c1323985
"""
import csv  # This loads the csv library.

def numberofnames(f):  # creates a function
    counter = 0
    f = open('classtestdata.csv', 'r')  # opens a csv file in read mode
    for line in f.read().split('\n'):
        counter = counter + 1
    csvdata = csv.reader(f) # Creates a csv reader object  
    data = [int(row[0]) for row in csvdata]  # Converts the csv reader object to data
    f.close()
    return counter
    

