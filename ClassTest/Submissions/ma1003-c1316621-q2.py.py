"""
Class test - question 2
c1316621
"""
import csv # This loads the csv library

out = open("classtestdata.csv", 'rb') # opens the data file in readable mode
data = csv.reader(out)
data = [row for row in data] # Reads all the data in to a list
out.close() # closes file

print data

str1 = data
print len(data)
print 
