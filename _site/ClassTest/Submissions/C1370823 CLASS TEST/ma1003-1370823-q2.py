import csv

f = open('classtestdata.csv', 'r')  # Opening the classtestdata
csvread = csv.reader(f)
data = [e for e in csvread]  # data = item for each item that is in classtestdata

print len(data) #  Printing how many items there are
data2 = [e for e in set(csvread)]  # data2 = item for each item that is in class test data without duplicates   
print len(data2)  #  Attempting to print this

r = 0
data1 = (len(e) for e in csvread)  #  Data1 = length of item for each item in class test data
data3 = (int(e) for e in data1)
print data3

print int(data1)/len(data)




