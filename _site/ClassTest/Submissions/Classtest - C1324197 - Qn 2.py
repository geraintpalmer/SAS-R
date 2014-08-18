import csv  # this is telling the computer what type of file it is

f = open ('classtestdata.csv', 'r')  # this opens the csv file in reader mode
classdata = f.read()

data = classdata.split('\n')  #This splits the data into a list of strings

print len(data)  # This prints the number of strings (names) in the list of data

def mean(x, y):
    """
    A function to return the mean legnth of names in the list of data

    Arguments:
        x which is the data as characters not split into strings
        y which is the data as a list of names

    Output: The mean legnth of all the names in the list
    """
    return len(x) / len(y)

print mean(classdata, data)  # This returns the mean legnth of name in the list.

print len([e for e in set(data)]) # This prints the number of unique neames in the file
