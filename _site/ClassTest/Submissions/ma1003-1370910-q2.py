import csv

textfile = open('classtestdata.txt', 'r') #opens a file in read mode
string = textfile.read() #reads the file as a string
data = string.split('/n')   #split method
textfile.close()

print data

data = [int(e) for e in data[:-1]] # converting our string into an integer
print data

print len(data)

def myaverage():
    average = 0
    n = 0
for str in data:
    n += 1
    sum = n + str
    average = sum / len(data)

print myaverage


