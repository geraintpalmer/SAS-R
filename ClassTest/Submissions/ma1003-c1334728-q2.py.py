"""
Class test - question 2
c1334728
"""


import csv  #imports csv library
names = open("classtestdata.csv", 'r')  #opens csv file
data = names.read()
data = data.split("\n")  #splits data into a list (from seperate lines)
data = data[:-1]  #removes the final element from data
names.close()  #closes the file


print len(data) #prints length of data(how many names there are)

for i in range(0, len(data)):
    sum1 = len(data[i])
    mean = mean / (len(data))
print mean

        
