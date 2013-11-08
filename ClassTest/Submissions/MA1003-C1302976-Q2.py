"""
Class test - question 2
C1302976
"""
import csv  

out = open("E:\Uni Work\computing for maths\class test\classtestdata.csv", "rb")  #This tells python where the csv file is located on my computer and the 'rb' tells it that we will be reading the file not writing to it
data = csv.reader(out)
data = [row for row in data]  #This slpits up my 
out.close()  
print data
print len(data)  #This tells me how many names there are in total in my csv file



