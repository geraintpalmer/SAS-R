import csv

def totalnames():

    """
    A fuction to retrun the total number of names in the file data

    Argumets: file data (names)

    outputs: length of list of file data
    """
    return len(e for e in csvdata)
    
    
def meanname():
    """
    A function that returns the mean length of names in the file data

    Arguments: length of names

    output : (Sum of total length of names)/number of names
    """

    return (sum len(e for e in csvdata))/len(csvdata)

def uniquenames():
    """
    A fuction that returns 
    """
    
    print[(len(e for e in set data)]
    
f = open ('classtestdata.csv', 'r')
csvdata = csv.reader(f)
data = [row for row in csvdata]
f.close()



