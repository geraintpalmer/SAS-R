"""
Class test- Question 2
c1329547
"""

import csv
f = open("classtestdata.csv",'r')
csvrdr= csv.reader(f)
data= [row for row in csvrdr] # read all data in to a list
f.close() #close file
print data

print len(data)
names =sentence.split()
verage = sum(len(name) for name in names)/len(names)


