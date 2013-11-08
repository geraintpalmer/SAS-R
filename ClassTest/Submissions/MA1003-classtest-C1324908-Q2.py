import csv  # Importing the data
f = open("classtestdata.csv", 'r')
csvrdr = csv.reader(f)  # Reads using csv library
data = [row for row in csvrdr] # Read all data in a list
f.close() # Close file

data = [str(row[0]) for row in data]  # Converts each row to a string

print len(data)
for row in data:
    len(row)  # Calculates the length of each row
    
i = 0  # set i = 0
k = 0  # set k = 0 
for i in range(len(data)):
    k += len(row)  # Adds the length of each row to k to obtain sum of all names
    i += 0
   
meanlengthofname = k / len(data) # Calculates the mean length of name for this data
print meanlengthofname


