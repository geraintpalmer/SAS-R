import csv

textfile = open('classtestdata.csv', 'r')# Opens a file in read mode
csvnames = csv.reader(textfile)    # Converts the textfile reader names to data
data = [row for row in csvnames]    #Read all data in the list
textfile.close()   #close file
data = [[str(e) for e in row] for row in data[1:]]   # Convert relevant data to string

print len(data)  # print length of names in the data

l = len(data)   # assign length of names in data to l

def meannames (a, b):
    """
this function calculates the mean of the length of names in data
Arguments :
a = length of names in data
b = values 2
Outputs :
the mean of length

"""

    if b == 2 :  # attribuates 2 to b
        return int ( a / b )  # the function will return integer of the division of a by b(by 2)
    return " no mean"  # if b is not 2 the function will return no mean

print meannames(l,2)

b = 789

print data [b] ## print a unique name

