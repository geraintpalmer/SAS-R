"""
Class Test - Question 2
c1315077
"""

names = open('classtestdata.csv', 'r') # This opens a file in read mode (hence the 'r')
string = names.read() # This reads the file as a string
#print string # This prints the list of names to the screen but as one big list
data = string.split('\n') # This line makes the interpreter display one name after the other instead of each one on a new line
print data

print len(data) # Prints the number of names in the list

words = string.split() # Defining the input
average = sum(len(word) for word in words)/len(words) # This defines the average and how it will work  
print average

"""
To show how many unique names, I'm turning the list 'data' into a set (which
removes duplicates, and then back into a list.
"""
newnames = list(set(data)) # Creates the new list
print len(newnames) # Prints the length of the new list therefore, the number of uniques
