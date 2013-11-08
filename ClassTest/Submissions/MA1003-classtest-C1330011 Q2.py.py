
textfile = open("classtestdata.csv", 'r')
string = textfile.read()
print string

data = string.split('\n') # splits up the data onto each row
print string

data = [[str(e) for e in row] for row in data[1:]] # prints the number of elements in the data
print len(data)

index = [[str(e) for e in row] for row in data[1:]]
print index
