

f = open('classtestdata.csv', 'r')   # opens the file in read mode
data = f.read()
f.close()

data = data.split('\n')   # splits each data into a new line

print len(data)  # prints length of the data

print len(data[0])


for l in data:
    r = len(data[0])
    

def mean(data):
    """
    Calculates the mean length of names in the list

    Arguments:
    length

    Output:
    mean length of names
    """
    N = r
    return len(data) / float(N)

print mean(data)

