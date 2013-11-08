import csv

out = open('classtestdata.csv', 'rb')  #Open the file in read mode
data = csv.reader(out)
data = [row for row in data]  #Converts the csv reader object to data
out.close()  #Close the file

print data  #Print the data in the csv file

print len[e for e in data]  #Print total number of names in the file

def avg(list):  #A function to calculate the mean length of names in the file
    sum = 0
    for e in list:
        sum += e

    print 'The average mean length of names in the file is %s' % e





