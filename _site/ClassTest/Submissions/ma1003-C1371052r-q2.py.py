import csv  # This imports the csv library

def namecount():
    """
    This function counts the number of names

    Arguments:
    names in csv file (number of rows)

    Output:
    an integer denoting the number of names in the file
    """


namecount = sum(1 for row in csv.reader( open('classtestdata.csv')))
print namecount  # Counts the number of names 

row = namecount
i = 1
for i in row, i > 0:
    row = str
    i += 1
    if i < namecount:
        type(str)
        
# Define each name
# Add len(eachstr)
# total len(allstr)
# meanlen = allstr / namecount

f = open ('classtestdata.csv', 'r')  # Opens and reads the csv file
cavrdr = csv.reader(f)
data = [row for row in cavrdr]
f.close()  # Closes the file

data = [[eval(k) for k in row] for row in data[1:]]
print sum(data) # Sums the data
    

 






