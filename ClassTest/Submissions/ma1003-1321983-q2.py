"""
solution to question 2 class test
"""

textfile = open("textfile.csv", "r") # opens the corresponding file in read mode
string = textfile.read() # reads the file
print string # prints the string to the screen

data = string.split("\n") # uses split method to create a list from the string, seperating on a given string
print data

print len(data) #prints the total number of names in the file


def averageLen(data):
    """
define the function to find the average length of data
"""
    lengths = [len(i) for i in lst]
    return 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths)) #mean length of names in file


def unique(data):
    """
find the number of names there would be if none of the names were repeated.
search file for number of names without counting repeated names
"""
    search
