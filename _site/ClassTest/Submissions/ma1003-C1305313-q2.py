"""
Class test - question 2
C1305313
"""

textfile = open('classtestdata.csv', 'r')  #opening file
string = textfile.read()
list = string.split('\n')
print len(list)  #prints the total number of names in list
