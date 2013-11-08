"""
Class test - question 2
c1322758
"""
import csv  # this loads the csv library
f = open("classtestdata.csv", 'rb')  # opens a file in reader mode 
data = csv.reader(f)  # creates a csv reader object
data = [row for row data]  # converts the csv reader object to data
print data  # the data is printed
print len(data)  # the number of values in the data is determined


for i in data:  # selects each individual component in the data
    print len(i)

