"""
Class test - question 2
c1312124
"""

textfile = open('classtestdata.csv', 'r')  # Opens the file in read mode
datalist = textfile.read()  # Reads the file
data = datalist.split('\n')  ~
data = [e for e in data[:-1]]
print data  # Prints the list of names

length = len(data)  # Assigns the variable length to the length of the data list
print "The total names in this list is %s" % length  # Prints out length of names

mean = (len(datalist)) / len(data)  # Setting variable mean to equal length of charcters divided by the total number of names
print "The mean length of the names is %s" % mean  # Prints mean length of names
