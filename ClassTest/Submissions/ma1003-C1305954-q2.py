"""

Class test - question 2
C1305954

"""

import csv #Imports file

f = open("classtestdata.csv", 'r') #opens file in reader mode.
csvrdr = csv.reader(f) 
data = [row for row in csvrdr] #Converts the data into a list of strings.
f.close() #Closes the csv file

print len(data) #prints the amount of names in the list.

lengths = [len(i) for i in data] #Defines the lengths to be the length of each name on the list.

print sum(lengths) / len(data) #Adds the length of each name and divides by the amount of names.

