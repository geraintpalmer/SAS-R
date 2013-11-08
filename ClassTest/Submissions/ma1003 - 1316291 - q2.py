import csv
f = open('classtestdata.csv', 'r')  #opens file
csvdata = csv.reader(f)  # reads file
data = [row for row in csvdata]  # reads all data into a list
f.close()  # close file
data = [[str(e) for e in row] for row in data]  # converts data into strings

print len(data)  # prints the number of names in the list


def meanlen(lst):
    """
    A function that will calculate the mean length of the names in the file
    using a boolean variable

    Arguments: e, each name, len(e) being the length of each name

    Outputs: the mean length of names in the file
    """
    lengths = [len(str(e)) for e in lst]  # this gives you the length of each name
    if len(lengths) == 0:
        return 0  
    else:
        return (float(sum(lengths)) / len(lst))  # this caculates the mean whereby, the sum of the length of each is divided by how many names there is altogether

print meanlen(data)  # prints mean length of names


def uniqueness(lst):
    
    
    
