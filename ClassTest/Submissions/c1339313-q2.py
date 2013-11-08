import csv
data = open('classtestdata.csv', 'rb')
newdata = csv.reader(data)
print newdata
