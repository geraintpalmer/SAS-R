f = open('classtestdata.csv', 'r') #opens file in reader mode
string = f.read() #imports data as string
f.close() #closes file
#print string


data = string.split('\n') #converts string to a list of "elements" of data

#print data #prints list of data


print len(data) #prints number of elements of data (number of rows in original file)

print (int(len(string)) / (int(len(data)))) #prints length of string (number of characters) divided by length data (number of names)


 

print len([e for e in set(data)])  # Uses the set function to remove repeats from the data, prints number of unique names
