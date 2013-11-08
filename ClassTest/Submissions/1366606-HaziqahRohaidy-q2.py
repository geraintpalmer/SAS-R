textfile = open('classtestdata.csv', 'r')
string = textfile.read()  # Reads the file, NOTE that this reads the file as a string, so the '\n' for new lines are also read.
data = string.split('\n')  # Splits the file on the newline character
#data = [int(e) for e in data[:-1]] # Removes last line and converts to integer

data = data[:-1] 
print len(data)
 
a = data
a = str(a)
#print a

def mean():
    return a / len(data)

print mean()


