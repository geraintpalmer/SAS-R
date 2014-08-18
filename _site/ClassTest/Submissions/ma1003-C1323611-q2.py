import csv
f = open('classtestdata.csv', 'r')
csvdata = csv.reader(f)  
data = [row for row in csvdata] # read all data in list
f.close()
data = [[str(e) for e in row] for row in data]  # converts each row into a string 

print len(data) # total names in file    

def meantotalnames():
    k = 0
    length = [len(str(e) for e in row(1))]  # length is equal to the len of first string in row 1
    if length > 0:  # if length is bigger than 0
        k += length  # add length to k
    else k += 0  # otherwise add nothing to k
print k

mean = k / len(data)  # mean is k (length of all names) divided by number of names in data
        

def uniquenames():
    counter = 0  
    if e in data == 1:  # if e(name) appears once
            counter += 1 # add one to counter for every unique name
    return counter  # otherwise return counter
print counter  # print counter which is number of every name that appears once
