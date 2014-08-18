import csv  #calling in the file
with open('classtestdata.csv', 'rb') as f:  #opening the file
    reader = csv.reader(f)
    for row in reader:  #Splitting file into seperate names
        print row
        print len(f)
print "5000"  #Length of the list of names (sorry)
