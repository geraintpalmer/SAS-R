"""
Class Test - question 2
C1325167
"""
import csv # Line opens the csv file in read mode ('r')
f = open("classtestdata.csv", 'r') #Line defines a csv reader to read file f
csvrdr = csv.reader(f) #Line reads each row from the csv file and adds it to list 'data'
data = [ row for row in csvrdr ]
print len(data)
f.close()

