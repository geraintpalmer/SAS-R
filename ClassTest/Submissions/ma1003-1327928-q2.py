"""
Class test - question 2
C1327928
"""



import csv   # Loads the csv library

textfile = open('classtestdata.csv', 'r')   # Opens a file in read mode
csvobject = csv.reader(textfile)  # Creates a csv reader object
data = [str(row[0]) for row in csvobject]   # Converts the csv reader object to data
textfile.close()


print len(data)   # This prints the total number of names in the file



my_list = [data]
lengths = [len(i) for i in my_list]
def averageLen(lst):
    lengths = [len(i) for i in lst]
    return 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths)) 
   
