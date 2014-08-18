"""
Class test - question 2
C1353578
"""
import csv
"""
imports the csv module
"""

text = open('C:/Users/c1353578/Desktop/classtestdata.csv', 'r')
#opens the data file
list = csv.reader(text)

list = [row for row in list]
#reads the data into a list of names


print len(list)
#prints the number of names in the list

text.close()
#closes the file

x = len(list)
y = 0
z = 0
for row in list:
    y = len(row[0])
    z += y
"""
creates a variable Z
for each name in the list, adds the length of the name to the variable
Z
"""
print z / float(x)

"""
takes the total length of all names, the variable Z
divides this number by the number of names, variable x
to give a mean length for the number of names
float(x) takes a floating point value rather than just the integer value.
"""
