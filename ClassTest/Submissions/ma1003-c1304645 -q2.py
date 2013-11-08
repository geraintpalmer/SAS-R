"""
class test - question 2
C1304645
"""

import csv
out = open("classtestdata.csv", 'r')  #save doc as CSV... comes up on excel
csvrdr = csv.reader(out)  #goes through data and splits it up into different strings.
data = [row for row in csvrdr]  #assigns these strings to a list the list is called data
out.close()  #closes textfile



#print data  # prints the names
print len(data) #prints 5000

print "%s\n" %data  #splits up data
n = 0
for i in data:
    print len index.nS

