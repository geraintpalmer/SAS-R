import csv  # Import the csv library so that data can be imported

f = open("classtestdata.csv", "r")  # Open the csv file, classtestdata in reader mode
csvrdr = csv.reader(f)  # Using the csv library to read the file
data = [row for row in csvrdr]  # Read all data in to a list
f.close()  # Close the file

print len(data)  # Print how many names are in the list

s = str(data)  # Convert the list of data into a list of string
print len(s) / len(data)  # Calculates the mean length of name by taking the total length of names and dividing it by the total number of names


