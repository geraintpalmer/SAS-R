"""
class test - question 2
C1370388
"""

textfile = open('classtestdata.csv', 'r') # opens up the file in reader mode
string = textfile.read()
print string # prints the file, ie the list of names

data = string.split('\n') # changes the string to a list, separates string on a given character
                    
print len(data) # prints the length of the data

print len(string)/len(data) # prints the length of the string divided by the length of data

print len([e for e in set(data)]) # using set method to remove duplicates from the list and find the number of unique names in the file
