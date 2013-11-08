"""
Class test - question 2
C1324128
"""

import csv

f = open("classtestdata.csv", 'r')  
csvrdr = csv.reader(f)
data = [row for row in csvrdr]
f.close()

data.sort()  #sorts data into a column
length = len(data)  # Set length to be size of data

#data = [[eval(k) for k in row] for row in data[1:]] 
print len(data)
