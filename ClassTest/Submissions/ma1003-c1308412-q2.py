"""
Class test - question 2
c1308412
"""

import csv  # Import the library as can also be used to import data
    
f = open('classtestdata.csv', 'r')  # Opens the csv file
csvdata = csv.reader(f)
data = [row for row in csvdata]  # csv file is converted into a list
f.close()

print len(data)  # Prints the number of names in the file


    
    

    
    
