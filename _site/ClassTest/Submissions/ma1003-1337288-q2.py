import csv		#Imports the csv library.

f = open('classtestdata.csv', 'r')		#Opens my csv file in read mode and calls it f.
csvdata = csv.reader(f)		#Uses the built in reader method for csv files and calls it csvdata.
data = [row for row in csvdata]		#For each row in csvdata which is the rows in our file, it will add each row as an element into a list called 'data'. 
f.close()		#Closes our original file once we have a copy of all of its data.

print "The total number of names in the file is %d.\n" %len(data) #Prints how many names are in the list using 'len' of our list which gives the number of elements in the list.

totallength = 0		#Creates a variable for the total length of the names in the file.
for e in data:		#Loops through each element in the list.
	totallength += len(str(e))		#Add the length of the string for each element to the total length.
	
print "The average/mean length of names in the file is %d.\n" %(totallength/len(data)) #Prints what the average/mean length of the names using the fact that mean is the total divided by the number of elements.

uniques = []		#Creates an empty list of unique names.
for e in data:		#Loops through each element in the list.
	if e not in uniques:		#If an element is not in my unique list it will be appended to the list uniques.
		uniques.append(e)
#If an element already exists in unique list then another will not be added.
		
print "The number of unique names in the file is %d.\n" %len(uniques)		#Prints the number of unique names using 'len' / number of elements in my unique list.
