textfile = open('classtestdata.csv', 'r')
string = textfile.read()
data = string.split('\n')
print data
print len(data)

    
