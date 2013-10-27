"""
Solution to question 2 of class test
"""

import csv  # Library to read the csv file

def mean(lst):
    """
    A function to return the mean of a list

    Arguments: a list

    Output: the mean value of that list
    """
    return sum(lst) / float(len(lst))


f = open('Data/classtestdata.csv', 'r')  # Open file in reader mode
csvrdr = csv.reader(f)  # Create a csv reader object
data = [row[0] for row in csvrdr]  # Read in parsed data
f.close()  # Close f

print len(data)  # Print the number of names in the list

print mean([len(n) for n in data])  # Prints the mean of length of the names in the list

print len(list(set(data))) # This is a python one liner, student may also:

uniquenames = []  # Create an empty list for unique names
for n in data:  # Iterate through every element of data
    if n not in uniquenames:  # if element is not in list
        uniquenames.append(n)  # Append it

print len(uniquenames)  # Print len of unique names
