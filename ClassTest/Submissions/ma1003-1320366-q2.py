"""
Class test - question 2
c1320366
"""
import csv #importing csv library

out = open("classtestdata.csv", "rb") # Opening the CSV file containing names
data = csv.reader(out) # Reading the CSV File that has been opened previous
data = [row for row in data]
out.close() # Closes the CSV File

print len(data) # Prints the length of the data


