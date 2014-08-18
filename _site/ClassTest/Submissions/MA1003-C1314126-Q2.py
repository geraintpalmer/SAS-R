"""
Class test - question 1
C1314126
This question involves importing a sheet of data with a list of names on it.
"""
textfile = open('classtestdata.csv', 'r')
data = textfile.read()
textfile.close()

data = data.split('\n')
print data

alist = data
print len(alist)  # This shows how many total names are in the list

list.count(obj)



