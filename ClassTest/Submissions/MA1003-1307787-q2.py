"""
Class test - question 2
c1307787
"""
import csv # Am importing library this library as it can also be used to import data

f = open("classtestdata.csv", 'r')
csvrdr = csv.reader(f) # Easier to read using csv library than manually
data = [row for row in csvrdr] # Read all data into a list
f.close() # Close file

print len(data) # Printing length of the list

new_data = [[int(len(k)) for k in row] for row in data] # Converting length of each individual name into an integer
print new_data # Now i need to sum all the elements in new_data and divide by len(data) but im not sure how to

