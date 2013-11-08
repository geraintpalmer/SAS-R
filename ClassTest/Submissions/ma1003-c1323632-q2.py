"""
Class test - Question 2
c1323632
"""

import csv
f = open("classtestdata.csv", 'r')  # Opens the file
csvrdr = csv.reader(f)  # Reads the file
data = [row[0] for row in csvrdr]  # Read all data in to a list, but only the first element of each row is required
f.close  # Close the file as it's no longer needed

print "There are %i names in the list." %  (len(data))  # Print how many elements there are in data 

totallenght = 0  # Totallenght is the lenght of all the names
for i in data:
    totallenght += len(i)  # Adding the lenght of each names in data to the variable totallenght

meanlenght = totallenght / float(len(data))  # Finding the mean lenght of a name by dividing totallenght by the number of names

print "The names in the list have an mean lenght of %.3f." % (meanlenght)  # Print the mean lenght of the names in the list

data.sort()  # Data is sorted into order

numberofuniquenames = 1  # The first name is the first unique name in the list. 
lastuniquename = data[0]  # Setting a variable with the last unique name found
for i in data[1:]:  # For loop only needs to run from 2nd element as frist element has already been accounted for.
    if i != lastuniquename:  # Checks to see if current name is different from the last unique name found. 
        numberofuniquenames += 1  # As a new unique name is found, add 1 to the total of unique names. 
        lastuniquename = i  # As there is a new name found lastuniquename becomes i which is a new unique name. 

print "There are %i unique names in the list." % (numberofuniquenames)  # Print the number of unique names in the list.
