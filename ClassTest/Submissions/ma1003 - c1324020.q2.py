#Class test question 2
#c1324020


import csv

f = open('classtestdata.csv', 'r') #opens the csv file and reads through it
csvrdr = csv.reader(f)
data = [word for word in csvrdr] #goes through every row in the csv file
f.close()                   #closes the file

print len(data) #prints the length of the data i.e the number of names in the data

data = [type(e) for e in data[:]]

print len([e for e in set(data)]) #I want it to search through the data and each time a repeat name is drawn up remove it from the len.

