import csv  # Am importing this library as can also be used to import data 

f = open('classtestdata.csv', 'r') 
csvrdr = csv.reader(f)  # This is a harder file to read manually so using the csv library
data = [row for row in csvrdr]  # Read all data in to a list 
f.close()  # Close file

print "Total names in file: ", len(data)  # Here we find the number of names in the file by determining the length of the file.


print len([e for e in set(data)])  # Uses the set command to remove duplicates from data. Other approaches would make use of loops. 
 
print len(
