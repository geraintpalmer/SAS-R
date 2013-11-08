'''
Class Test
Quesion 2
Cl1226574
'''
import csv  # importing the csv module
sourcefile = open("classtestdata.csv", "r")  # opens in read mode
data = csv.reader(sourcefile)  # reads the sourcefile as a csv
data = [row for row in data]  
print len (data)
y = 0
for row in data:
    x = len(row[0])  # this gives the length of each name
    y += x   # adds all the lengths together

mean = (y/len(data))  # gives the mean 
print mean

for row in data:
    if row[0] != row[0]:
        print row[0]
