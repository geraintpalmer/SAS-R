"""
Class test - question 2
c1370909
"""
textfile = open("classtestdata.csv", "r")  # Opens a file in read mode
data = textfile.read()  # Reads the file
textfile.close()  # Closes data

data = data.split("\n")  # Splits the file on the newline character

data = [str(e) for e in data[:-1]]  # Removes last line and converts to string

print len(data)  # prints the total number of names in the data file

lengths = [len(i) for i in data]


def averagelen(lst):
    lengths = [len(i) for i in lst]
    return 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths))

lengths = [averagelen(i) for i in data]
print averagelen




def average_len(l):
    return sum(data(len, l))/float(len(l))

data(average_len, lengths)

print average_len
