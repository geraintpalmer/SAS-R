"""
Class Test - Question 2
C1334215
"""

textfile = open('classtestdata.csv', 'r') #importing the data file, open the file in 'read mode'
string = textfile.read() 
textfile.close() #close file
print string

string = string.split('\n') # Split on new lines
print string

print len(string) #total amount of names are in the data file


