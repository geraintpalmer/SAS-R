import csv  #import csv library
file = open('classtestdata.csv', 'r')  #open the csv file in read mode
csvrdr = csv.reader(file)
data = [row for row in csvrdr]  #create list 'data' from each row in file
file.close()  #close file

print('Number of names: %i') % (len(data))  #print the number of names in list

length = 0  #initialise integer variable 'length'
for i in range (0, 4999):  #for each element in the list 'data'
    length += len(str(data[i]))  #add the number of characters in each string to 'length'
print('Mean length: ' + str((length/5000)))  #print length divided by no of elements

def compare(string1, string2):
    if len(string1) == len(string2):
        for i in range(0, len(string1)):
            if string1[i] == string2[i]:
                return True
    else:
        return False
'''
Takes two strings and first compares their lengths
if lengths match then compares each letter in string
if each string is identical returns true
'''
    
unique = 0  #initialise unique variable to 0
flag = False
for i in range (0, 4999): #for each element in the list 'data'
    for i in range (0, 4998):   #for each element in the list 'data'
       if not compare(data[i], data[i+1]):  #if the strings are not the same
           flag = True  #set flag to true
    if flag == True:
        unique += 1  #if flag is true increment unique

#i know this doesnt work

print('Unique names:' + str(unique))  #print number of unique names
