"""
Class test - Question 2
C1311689
"""

import csv

f = open('C:\Users\c1311689\My Documents\Downloads\classtestdata (2).csv', 'r') # Opens file
csvrdr = csv.reader(f)
data = [row for row in csvrdr]   # Reads all the data into a list
f.close()   # Close file

#print data
print len(data)  #Prints the total names in the list



