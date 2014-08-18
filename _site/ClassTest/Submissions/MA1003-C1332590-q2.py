"""
Class test - question 2
C1332590
"""

import csv

f = open("classtestdata.csv", "r")  #this will open the file and read it, so will import the data
csvrdr = csv.reader(f)
data = [row for row in csvrdr]  #this assigns the rows in the file to the variable data
f.close()  #closes the file


print len(data)  #This will return the legnth of the data, or the number of names in it

print (sum(len(row) for row in data)) / 5000


"""
This is my attempt at trying to get the mean legnth of names
I realise that each row is counted as legnth one, as i have not converted each row to a string
Unfortunately i didnt have enough time to convert each row to a string, this is what i would have done, had i had more time
"""

data = data.split()
data = [int(e) for e in data]
print len(data) / 5000  #this is me working in the last few minutes to try to turn the data into a string
