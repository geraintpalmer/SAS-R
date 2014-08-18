import csv

f = open("classtestdata.csv", "r")  #opens the file to python
csvrdr = csv.reader(f)
f.write("%s\n" % row)
data = [row for row in csvrdr]
f.close()

print len(data)  #prints how many names are in the data file


for row in data:
    data.write("%s\n" % row)
    print type(row)  
    length = len(row)

