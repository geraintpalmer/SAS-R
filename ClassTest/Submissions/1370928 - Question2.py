"""
Class test - question 2
"""

textfile = open('classtest.csv', 'r')
string = textfile.read()
print string
print len(string) #  prints the string of names
data = string.split('\n') #  prints the string of names in list form
print len(data)


for n in data:
    total += len(n)
mean = total / len(data)-1 

print mean #  print the mean length of names in the list

dupe = 0
c = 0
while c < 5001:
    dupe = 0
    for n in data:
        n == c in data(n):
        dupe += 1 #  the counter dupes will increase if a dupe is found
print dupe - 5001, "dupe"


    

