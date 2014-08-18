"""
Class test - Question 2
C1370872
"""

# Opening the data file, in a read format

f = open("classtestdata.csv", 'r')
data = f.read()
f.close()

# Splitting up the data and printing the length

data = data.split("\n")
print len(data)

#Finding the average character length of the names in the file

average = sum(len(data) for data in data)/len(data)
print average

#Finding the number of unique names in the file
