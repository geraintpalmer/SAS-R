"""
Class test - question 2
C1330232
"""

import csv  # importing the csv library so we can open our data using the cvv format

out = open("classtestdata.csv", "rb")
data = csv.reader(out)
data=[row for row in data]
out.close()

print data[:100]  # just checking our data

print len(data)  # we print the length of the list data to find out how many total names are in our data file



def meanlength(list):
"""
A function to give us the mean length of names

Arguments: a list with elements which we want to find the mean of

Outputs: mean length 
"""
    lengthofnames = []  #  an empty list which we will add the length of each name in data to
    for e in data[:100]:
       print len(e[0])
       lengthofnames.append(len(e[0]))
    return sum(lengthofnames) / len(lengthofnames)

# print meanlength(data)




