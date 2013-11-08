"""
Class test - question 2
c1308374
"""

import csv
f = open('classtestdata.csv', 'r') # opens a file in read mode
string = f.read() # reads file
data = string.split('\n') # splitting the file on the newline character
print data
print len(data)
print len

def unique(name):
    """
    A function to return whether a name is unique or not

    Arguments: n, a name

    Outputs: True or False
    """
    
    
    
    
