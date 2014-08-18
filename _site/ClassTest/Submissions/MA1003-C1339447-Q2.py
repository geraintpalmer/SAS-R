"""
Class test - question 2
C1339447
"""
textfile = open('classtestdata.csv', 'r')  # this will open the file in read mode
string = textfile.read()
data = string.split('\n')
print "There are %i names in the file." % len(data)

meanlength = len(string) / float(len(data))
print "The mean length of names in the file is %.2f letters." % meanlength

