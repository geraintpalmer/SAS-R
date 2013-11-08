import csv


f = open('classtestdata.csv', 'r') #opening file using csv library
csvdata = csv.reader(f)
data = [row for row in csvdata]
f.close()
print data

print "total number of names in data file is %s" % len(data)    #printing number of names in file

print "mean length of names in file is %s" % data(characters)/float(len(data))      #mean numbers of characters per name

for row in row of data[
def samenames(self, data):
    del self.data[self.data.index(data)]


print "number of unique names in the file is %s" % unique(data)
