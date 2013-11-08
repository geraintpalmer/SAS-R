import csv                           # importing the data
f = open ("classtestdata.csv", 'r')  # opening file in readermode
csvdata = csv.reader(f)
data = [row for row in csvdata]
f.close()                            # closing file.

print len(data)  # prining the length of the data file


print data
data2 = data.split('\n')
print data




