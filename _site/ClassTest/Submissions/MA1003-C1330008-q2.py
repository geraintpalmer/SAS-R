"""
Class test - question 2
C1330008
"""

import csv

f = open("classtestdata.csv", 'r')  # open and read file saved on USB
csvrdr = csv.reader(f)  
data = [row for row in csvrdr]
f.close()  # split data into rows and close the file

print data


print len(data)  # return the amount of rows contained in the file



