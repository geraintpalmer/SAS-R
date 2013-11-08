"""
class test - Q2
c1335028
"""
import csv  #importing this library
f = open("classtestdata.csv", "r") 
csvrdr = csv.reader(f)
data = [row for row in csvrdr] # reading all data into a list
f.close() #closing file
data = [[e for e in row] for row in data]

print len(data) # tells us how many names are in the file


