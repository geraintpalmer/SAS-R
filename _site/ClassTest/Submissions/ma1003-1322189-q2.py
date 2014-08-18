"""
Class test - question 2
c1322189
"""

import csv

f = open('classtestdata.csv', 'r')  # this opens the file in read only
csvdr = csv.reader(f)
data = [row for row in csvdr]
f.close()

print len(data)  # this counts how many strings are in the list



print data

i = 0
s = 0
while i < len(data):

