"""
Class test - question 2
C1260652
"""

"""
A function to read data from a file and print the amount of names, the mean length of names and the number of unique names in the file

Arguments: n (the information in the file)

Outputs: the number of names, mean length of names and number of unique names 
"""

textfile = open('classtestdata.csv', 'r')  # Open file in reader mode
string = textfile.read()  # Create a string of the data contained in the file
data = string.split('\n')  # Separate the string on the given character

print len(data)  # Print the amount of names in the file

i = data  # i equals the names in the file
print len ([i for i in 'classtestdata.csv' if f.unique()])  # Find the mean length of the names in file


