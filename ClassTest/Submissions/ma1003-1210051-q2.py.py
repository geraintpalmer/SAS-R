textfile = open('classtestdata.csv', 'r')  # opens the desired file in read mode
string = textfile.read()  # reads the file as a string
data = string.split('\n')  # uses list method to create a list from a string
print "There are %s names in the list" % (len(data[:-1])) # print length of created list of names minus the last empty one
print "There are %s unique names in the list" % (len(set(data)))  # set function finds the unique names and disregards repeats
numberofnames = len(data[:-1])

mean = len(string)/numberofnames  # divides length of total names by the number of names to get the average length of the names

print mean

