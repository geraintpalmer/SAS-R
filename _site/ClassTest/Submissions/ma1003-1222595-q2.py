'''
Class test - question 2
C1222595
'''
import csv 


textfile = open('classtestdata.csv', 'r')  # Opens a file in read mode
csvobject = csv.reader(textfile)  # Creates a csv reader object 
data = [str(row[0]) for row in csvobject]  # Converts the csv reader object to data

print len(data) #prints how many total names are in the data file


    



