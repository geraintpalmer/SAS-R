"""
Class Test - Question 2
C1326829
"""

import csv                                      #Imports the CSV library to aid with the opening of CSV files
f = open("classtestdata.csv", 'r')              #Creates a machine that can read the csv file
csvrdr = csv.reader(f)  
data = [row for row in csvrdr]
f.close()                                       #The data has now been stored in the variable data so the connection to the file can be closed
data = [[k for k in row] for row in data[1:]]   #Appends the data to a list

print 'There are',str(len(data)), 'names in this data.'     #Prints the length of data

count = 0                                       #Initalise count at 0
for e in data:                                  #For every element in data
    count += len(e[0])                          #Add the number of characters in each name to count
print 'There is a mean of',str(count / len(data)),
print 'chracters per word in this data'         #Print the number of chracters across all names divided by the number of names, this is a calculation for the mean number of characters in each name.

count = 0                                       #Reinitialise count at 0
for f in data:                                  #For every element in data
    if data.count(f[0]) == 1:                   #if the shell counts 1 instance of f in data, then it is unique,
        count += 1                              #So increment count by 1
print 'There are',str(count),'unique names in the data.' #print count
    
