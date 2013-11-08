"""
Class test - question 2
C1338020
"""

def getData(filename):
    """
    Reads data in from file

    Arguments: filename - a string containg the filepath to the data file

    Output:     data - a list that contains all the names in the file
    """
    sourcefile = open(filename, 'r')            # Open the data file
    data = []                                   # Create an empty list to store the data in 
    for i in sourcefile.read().split('\n'):     # Go through each line and add it to the list
        data.append(i)
    data.pop(-1)                                # Remove last empty element
    return data                                 # Return the list of names 

def getNumberOfNames(data):
    """
    Returns the number of names in a list

    Arguments: data - a list containing the names

    Output: an integer which represents the number of names in the list
    """
    return len(data)

def getMeanNameLength(data):
    """
    Returns the mean length of names in the list

    Arguments:  data - a list containing the names to be processed

    Output: a number depictring the mean length of names in the list
    """
    namelength = []
    for i in data:
        namelength.append(len(i))           # Add the length of each element to a list
    return (sum(namelength)/len(namelength)) # Return the mean 

def getNumberOfUniqueNames(data):
    """
    Returns the number of names unique to the list proivided

    Arugments:  data - a list containg the names to be processed

    Output:     a number depicting the number of names unique to that file 
    """
    uniquenames = []                            # Create an empty list for the values to be stored in 
    for i in data:                              # For each item in the list provided
        for k in uniquenames:           
            if (data[i] == uniquenames[k]):     # Copmpare it with the items in the unique names list
                pass
            else:
                uniquenames.append(i)           # If different add it to the list and break the loop
                break
    print uniquenames
    return len(uniquenames)                     # Return the length of the unique name list 
            

data = getData("C:\Users\c1338020\Desktop\classtestdata.csv")
numberofnames = getNumberOfNames(data)
meannamelength = getMeanNameLength(data)
numberofuniquenames = getNumberOfUniqueNames(data)

print "Number of names in file %d" % numberofnames
print "Mean length of names in file %d" % meannamelength
print "Number of unique names %d" % numberofuniquenames 
