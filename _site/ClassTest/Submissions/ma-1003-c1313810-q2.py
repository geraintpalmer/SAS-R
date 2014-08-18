"""
Class test - question 2
C1313810
"""


import csv  # loads the csv library

csvfile = open("classtestdata.csv", 'r')  # opens the csv file in read mode
data = csvfile.read()  # reads what's in the file as a string
csvfile.close  # close the csv file


data = data.split("\n")  # split each string onto a new line
print len(data)


lengths = [len(i) for i in data]  # assigns the term lengths to the length of each element in the data list
print float(sum(lengths)) / len(lengths)  # prints the mean length of names in the file


mylist = []  # creates an empty list
for i in data:
    if i not in mylist:  # for each element that does not already appear in the data (i.e. is not repeated)
        mylist.append(i)  # add to mylist (empty list)
print mylist
