textfile = open('classtestdata.csv', 'r')  # Opens the file in read mode
string = textfile.read() # Reads the file as a string

data = string.split('\n')  # Creats a list from the string by splitting each part of the file up
print len(data)  # Prints the length of this list

print len(string)/len(data)  # Prints the number of charachters/ length of list, giving a mean length of file names
