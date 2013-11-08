"""
Class test = question 2
c1304922
"""

f = open("classtestdata.csv", 'r')   # Open a file in read mode
data = f.read()   # Read the data as as string
f.close ()   # Close the file

data = data.split("/n")   # Split on new lines
print data

for line in f:
    words = line.split() 
    total += len(words)   # Add one to the lenth each time
print total

lstLines = f.read().split('/n')
dic((name,lstLines.count(name)) for name in lstLines)
lstLines.count('name1')



#f = ()
#for f in data:
    #f.append(len(data))

i = 0
s = 0
while i < len(data):
    i += 1
    s += 1
print s


def average(names):
    return sum(names)/len(names)
#sentence = input(The average length of names are: ")
words = sentence.split()
lengths = [len(word) for word in words]
print 'Average length:', average(lengths)


data = [float(n) for n in my_file.read().split()]
data = []
total = sum(data)
average = total / len(data)
print average
    
