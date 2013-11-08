
#first we need to import the csv file and make it readable form for python#

import csv

f = open("classtestdata.csv", 'r')
csvrdr = csv.reader(f)
data = [row for row in csvrdr]
f.close()

#print data would print all the names out#



#first we need to convert aech string into a integer data form. if we say each string has
the value of 1, and we sum up all the strings, then we will find out the total
number of  names in the data file#


def insertionsort(data):
    firstUnsorted = 0
    while firstUnsorted < len(data) - 1:
        indexOfSmallest = firstUnsorted
        index = firstUnsorted + 1
        while index <= len(data) - 1:
            if data[index] < data[indexOfSmallest]:
                indexOfSmallest = index
            index += 1
        data[firstUnsorted], data[indexOfSmallest] = data[indexOfSmallest], data[firstUnsorted]
        firstUnsorted += 1



