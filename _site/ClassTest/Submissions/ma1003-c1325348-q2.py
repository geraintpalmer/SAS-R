'''
Class test - question 1
c1325348
'''

import csv # This imports the csv library

textfile = open('classtestdata.csv', 'r') # Opens file in read mode
csvobject = csv.reader(textfile) # Creates a csv reader object
textfile.close() # Closes the file


data = string.split('\n') # This transforms the string to a list which separates a string on a given character
print data

def mean(n):
    '''
    This creates a function to return the mean of a list

    Arguments:
        lst: A list of numbers

    Outputs:
        The mean
    '''
    sumofelements = sum(lst)
    N = len(lst)
    return lst / float(N)

print len([e for e in textfile]) # Prints to screen how many total names are in the data file
print mean([e for e in textfile]) # Calls the mean function to find the mean length of names in the file




