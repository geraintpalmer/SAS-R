"""
Class Test - Question 2
C1311649
"""

import csv

f = open('classtestdata.csv', 'r') #This opens the file
csvdata = csv.reader(f)
data = [row for row in csvdata]
f.close()                        #All this code is reading the file and copying it as variable data.

n = 0
for row in data:
    n += 1

print n

e = 0
for i in range(1, n):
    n = len(n)
    e = e + len(n)
    mean = e / n

print mean

