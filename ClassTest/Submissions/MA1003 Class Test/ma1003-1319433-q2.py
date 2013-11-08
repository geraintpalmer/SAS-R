"""
Class test - question 2
c1319433
"""
import csv  # importing this library as can also be used to import data
f = open("classtestdata.csv", 'r')  # open file
csvdata = csv.reader(f) 
data = [row for row in csvdata]
f.close()  # close file


totalofnames = csvdata.readline(n)  # Assign 
print totalofnames

length = len(data)  # set length to be size of data 
print length

reader = csv.reader(open("classtestdata.csv"))
count = 0;
for row in reader:
    count+=1
    print "total no in row "+str(count)+" is "+str(len(row))
    for i in row:
        print i
