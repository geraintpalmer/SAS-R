"""
Solution to Q2 of the class test.
This question asks us to import the csv file and find out certain things about the data such as how many total names are in the file,
the mean lenght of names in the file and the number of unique names in the file

"""
import csv # This loads the csv library. Good practise in programming.

def totalnames(n):
    """
    This function to return the total number of names in the csv file

    Arguments: m, an integer

    Outputs: n, an integer

    """
    return len(csv) % e (names) #If I print the entire lenght of the list and then divide that number by how many elements are in the list, I will get the total number of names
textfile = open('classtestdata.csv', 'r')  # opens the file in read mode
csvobject = csv.reader(textfile)  # This creates a csv reader object
data = [e(row[0]) for row in csvobject]  # converts the csv reader object to data
textfile.close()

print len([e for e in data if e(str)])# print the length of every element in data providing its a string

def uniquename(n):
    """
    this function returens how many unique names are in the list
    e.g a name that we do not see twice

    arguments: m, an integer

    Output: m , an integer
    """"
    if name in list == 1:
        return 'unique name':  # if there is only 1 name of this kind in the list
            n +=1  # the number of names in our list increases by one
        
