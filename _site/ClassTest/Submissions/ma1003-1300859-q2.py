"""
Class test - question 2
c1300859
"""

import csv  #importing this library as it can import data 

f = open('classtestdata.csv', 'r')
csvdata = csv.reader(f)  # using csv library
data = [row for row in csvdata]# Read all data in to a list
data = [[str(e) for e in row] for row in data]
f.close()  # Close file

print "There are %i names in the file" % (len(data)) #prints the number of names calculated by the lenth of the list

def meanofnames(data):
    '''
    A function to calculate the mean of the length of the names in the csv file

    Arguments: list of names

    Outputs: the mean length of names
    '''
    n = 0
    for e in data:
        n += len(e)
    return n / len(data)


print "The mean length of the names is %i" % (meanofnames(data))

def unique(data):
    '''
    A function which finds how many unique elements are in a list

    Arguments: list of names

    Outputs: How many only occur once
    '''
    newlist = []
    for e in data:
        if e not in newlist:
            newlist.append(e)
        
    return len(newlist)

print "The number of unique names is %i" % (unique(data))
