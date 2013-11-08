# Class Test Question 2 C1370929

import csv  #letting python know i am importing a csv file


class Listofnames():
    """
    Contains a list of different names
    """
    
f = open('classtestdata.csv', 'r')  # Opening the file in read mode
csvdata = csv.reader(f)  # Using csv library to read as easier
data = [row for row in csvdata]  # Makes all data into a list of seperate names where the names are as variables rather than just being seperated by commas
f.close()  #this closes the file


print len(data)  # This tells us how many names are in the list

count = 0

def Listofnames():
    for data in reader:
        count += 1

print count
