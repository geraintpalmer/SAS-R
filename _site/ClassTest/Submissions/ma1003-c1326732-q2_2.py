import csv
textfile = open('classtestdata.csv', 'r')
csvobject = csv.reader(textfile)
data = [str(row[0]) for row in csvobject]
textfile.close

numberofnames = 0
for row in data:
    numberofnames +=1

print numberofnames

totalcharacters = 0
for row in data:
    length = len(row)
    totalcharacters += length

meanlength = totalcharacters / numberofnames
print meanlength

