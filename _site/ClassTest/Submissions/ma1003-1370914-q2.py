import csv  # Imports the csv module

data = open("classtestdata.csv","r")  # Opens the csv file in read mode
#split.data('/n')
names = csv.reader(data)  # Reads the data and makes it 'names'
names = [row for row in data]  


print len(names)


def mean(lst):
    """
    A function that produces the mean length of data in a list

    Arguments: lst: a list

    Outputs: The mean length of all elements in the list
    """
    for int(i) in names:  # For every element in names
        total = 0
        total += len(i)  # Add to total the length 
    return total / sum(len(names))
    
