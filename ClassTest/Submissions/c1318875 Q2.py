"""
Class test - question 2
c1318875
"""

import csv #this loads the csv library

textfile = open('classtestdata.csv', 'r') #opens a file in read mode
string = textfile.read() #reads the file, as a string
data = string.split('\n') #this uses the split method which creates a list from a string, seperating on a given string

print len(data) #computes the length of how many names are in the data file

average = sum(data)/len(data) #calculating the mean of the data file
print average

for i in data:
    print("total number of unique names", (i, data[i])) #totaly number of unique names
    

