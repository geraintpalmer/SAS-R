import csv

textfile = open('classtestdata.csv', 'r')  
string = textfile.read()  
data = string.split('\n')  
data = [str(e) for e in data[:-1]] 

print data
print len(data)

print [len(e) for e in data]

def meanlength(data):
    s = 0
    l = 0
    for e in data:
        while l < len(data):
        s += len(e)
        l += 1
    return s / len(data)

meanlength( e for e in data)


