textfile = open('classtestdata.txt', 'r')
data = textfile.read()
textfile.close()

data = data.split('\n')

data = [int(e) for e in data[:-1]]
print data

"""
the above code opens a file in read mode
and I declare it as a string
then I ask it to print the string
"""

words = sentence.split()
average = sum(len(word) for word in 'casstestdata.txt')/len(words)
"""
the above code will calculate the average length of each name in the data file"
"""

for line in lines:
    words_all = words_all + len(line.split())
print 'Total words:   ', words_all

"""
this would print total words if I knew how to define words_all"""

