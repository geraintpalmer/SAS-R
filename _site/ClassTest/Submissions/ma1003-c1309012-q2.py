"""
Class test - question 2
c1309012
"""

import csv   #this loads the csv library
textfile = open('classtestdata.csv', 'r')   #opens a file in read mode
csvobject = csv.reader(textfile)  #creates a csv reader object
data = [str(row[0]) for row in csvobject]  #converts the csv reader to object data 
textfile.close()

print len([e for e in data])  #gives the total number of names that are in the data file
print len([e for e in set(data)])  #gives the total number of unique names in the data file

