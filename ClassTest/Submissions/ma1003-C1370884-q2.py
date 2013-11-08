"""
Class test - question 2
C1370884
"""

import csv # Importing the file
f = open('classtestdata.csv', 'r') # Opening the file
csvrdr = csv.reader(f) # Reading the file
data = [row for row in csvrdr] # Making sure it uses all the data
f.close() # Close the file

print len(data) # Prints the ammount of data in the file





