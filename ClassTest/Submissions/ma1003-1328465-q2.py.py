import csv #This loads csv library
textfile = open('classtestdata.csv','r') # opens a file in read mode
csvrdr = csv.reader(textfile) #creates a csv reader object
data = [row for row in csvrdr] #converts the csv reader object into data
textfile.close()

data =([eval(k) for k in row] for row in data[1:]) #converts the data 
print data

print len(data) #prints the number of names in the data 
print len([e for e in set(data)]) #prints the number of unique name in the data

