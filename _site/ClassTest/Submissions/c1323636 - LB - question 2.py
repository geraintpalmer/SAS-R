"""
Class test question 2
c1323636
"""

textfile = open('classtestdata.csv', 'r') #this opens corresponding file in write mode
data = textfile.read() # allows file to be read
classnames = data.split('n')

print classnames # prints all data, the class names are all run on python.

class Namesdata():
    """
    A class for lits of names

    Attributes:
        Totalnames: how many total names are in the file data.
        Meanlength: the mean length of names in the file data.
        Uniquenames: the number of unique names in the file data.
    """

classnames = [] #initalize empty list
