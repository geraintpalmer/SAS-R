"""
class test - question 2
c1336772
"""


import csv   # this loads the csv library

textfile = open('classtestdata.csv', 'r') # opening the file in readmode
csvobject = csv.reader(textfile)   # creates a csv reader object
string = textfile.read()  # reads the file
textfile.close()        # closes the file

data = string.split('\n')   # this uses the split method which creates a list from a string, seperating on a given string
print data                  # printing data

print len(data)             # printing length of data


def namelength(string):     # defining a function to return the mean length of names in data
    meannames = []              # creating an empty list
    for i in range(5001):  # stating the range of data, as given in len(data) earlier
    eval(string)
    meannames.append(
    
return sum(namelengths) / len(numofnames)
