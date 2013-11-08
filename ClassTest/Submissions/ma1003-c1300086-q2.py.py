"""
class test question 2
c1300086
"""


import csv
out = open('classtestdata.csv', 'r')  # Opens a file in read mode (students must use correct path)
data = csv.reader(out)  # Creates a csv reader object (in essence this replaces the split approach from previously)
data = [row[0] for row in data]
out.close()

print data
print len(data)

#print len([e for e in data if func(e)])



