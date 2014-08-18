"""

Class test - Question 2
C1324536

"""

import csv # importing csv file that I have downloaded

out=open("classtestdata.csv","rb") # reading file
data=csv.reader(out)
data=[row for row in data]
data = data.split('\n')
data = [lst(e) for e in data[:-1]] 
out.close()

print data
print len(data) # total names that are in the file

def mean(data): # defining mean
    sumofelements = sum(data)
    N = len(data)
    return data / float(N)

print mean

"""

Importing csv file
Reading file
Printing list of data
Printing the total names that are in the file
Defining mean
Printing the mean length of names in the file

"""
