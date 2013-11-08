import csv

f = open("classtestdata.csv", 'r')
csvrdr = csv.reader(f)
data = [row for row in csvrdr]
f.close()

print data

alist = ["classtestdata.csv"]
print len(alist)
#prints how many total names are in the file
print len(max(alist)) + len(min(alist)) / % 2
#prints the average length of names in the file
