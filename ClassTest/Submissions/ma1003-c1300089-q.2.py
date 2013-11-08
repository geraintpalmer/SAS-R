import csv

f = open('classtestdata.csv', 'r')
csvdata = csv.reader(f) #  using csv library to read data
data = [row for row in csvdata] #  read all the data in thge list


print len(data) #  this prints the total number of names



