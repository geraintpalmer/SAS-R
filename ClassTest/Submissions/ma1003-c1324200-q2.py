"""
this opens a list of data and reads the data in the list
"""
textfile = open('classtestdata.csv', 'r')

data = textfile.read()

textfile.close()

data =data.split('\n')

a= data
print len(a)# prints the number of names in list

b= int(a)
print (b/len(a))
