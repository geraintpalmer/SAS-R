#Exam question 2
import csv

f = open("classtestdata.csv", "r") #Opens file.
csvrdr = csv.reader(f) # reads file.
data = [row for row in csvrdr] # makes data = file.
f.close() # closes file.
data = [[str(k) for k in row] for row in data[1:]] # makes all of the names into a string in the row 1.

print len(data) # prints length of data.

data2 = [[int(k) for k in row] for row in data[1:]] # changes all of names into the sum of letters.

print(sum(len(data))/len(data)) # sum of letters/length of data.


