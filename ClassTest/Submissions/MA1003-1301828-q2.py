"""
    Class test - question 2
    c1301828
"""

import csv
f = open("classtestdata.csv", "r") # this imports the file into reader mode
csvdata = csv.reader(f)
data = [row for row in csvdata] # Reads all of the data (names) into a list 

f.close() # close the file

number_of_names = len(data) # claculates the length of the list
print "The number of names in this list is %i" % number_of_names # prints the number of names

length_words = [len(i) for i in data]

def average_len(data):
    """
     A function which calculates the length of the names in the list

    Attributes:
        data: the list of names
    Outputs:
        length of words in list
    """
    length_words = [len("\n") for i in data]
    return 0 if len(lenght_words) == 0 else (float(sum(length_words))/len(length_words))
print length_words


matching = [] #create an empty list 
unique = [] # create an empty list 
for i in data:
    if i == i: # if two names are the same then put them in the latching list 
        matching.append(i)
    return len(matching)

number_of_matching = len(matching) # claculates the length of the list

print "number_of_names - number_of_matching" % (number_of_names, number_of_matching) # calculates the number not not maching i.e. unique
