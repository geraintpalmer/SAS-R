import csv  # import csv library

f = open("classtestdata.csv","r")   
csvdata = csv.reader(f)   
data = [row for row in csvdata]   # convert data into a list
f.close()   # close file


print "There is %s names in this list of data" % (len(data))  # print how many names in data

r = 0   # create a counter
for i in data:   # for names in data
     r + len(i)   # sum the amount of letters in name

meanlength = (r / len(data))   # the sum of all lengths of names divided by the amount of names
print meanlength

print len([i for i in set(data)])   # prints unique names
