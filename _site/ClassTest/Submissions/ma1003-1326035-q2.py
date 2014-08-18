
textfile = open('classtestdata.txt', 'r')
string = textfile.read()
print string


data = string.split('\n')
print data

data = [int(e) for e in data[:-1]]



