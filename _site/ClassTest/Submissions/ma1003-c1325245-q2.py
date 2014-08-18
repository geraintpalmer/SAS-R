import csv #importing the csv module

f = open("classtestdata.csv", 'r') # opening my csv file in a read only format
csvdr = csv.reader(f)
data = [row for row in csvdr] # creating a list which holds every row of data
f.close() # closing the csv module
print data # printing my list of names in python that were gathered from the csv file

print len(data) #printing how many names are in the list

print((len(data[0:]) for row in data[0:])/(len(data))) # an attempt at finding the mean


