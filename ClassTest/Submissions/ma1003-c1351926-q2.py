
"""

class test - question 2
c1351926
"""

textfile = open('classtestdata.csv', 'r')
string = textfile.read()
print string #  prints the string of names
data = string.split('\n') #  splits the string of names into a list
print "number of names:" , len(data)-1 # prints number of names in file

#print data
total = 0
for n in data:
    total += len(n)
mean = total / len(data) #  sum of total length of names / number of names = mean
    
print "mean lentgh of names:" , mean # mean lentgh of names

