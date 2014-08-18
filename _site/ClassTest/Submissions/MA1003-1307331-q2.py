import csv      # This loads the csv library.

file = open("classtestdata.csv", "r") # This file is opened in 'read' mode.
data = csv.reader(file)         # Creats a csv reader object
data = [row for row in data]    # Converts the csv reader object to data.
file.close()                    # Closes the file.

print data                      # Prints data from file.

print len(data)     # This will print the total number of names in the file


