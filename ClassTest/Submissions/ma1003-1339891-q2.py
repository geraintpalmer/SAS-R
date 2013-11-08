"""
Class test - Question 2
C1339891
"""

import csv  #imports csv module

classtestdata = open('classtestdata.csv', 'r') #opens file in read mode

classtestdata = csv.reader 
classtestdata = (row for row in classtestdata)
print len(classtestdata) #prints the number of names there are on the list

