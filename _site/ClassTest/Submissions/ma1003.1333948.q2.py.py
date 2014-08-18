f = open("classtestdata.csv", 'r')  #open the textfile in read
string = f.read()  #reads the file and makes it into a string
f.close()  #closes the file

integer = len(string)  #saves as the amount of integers in the all the names
string = string.split("\n")  #splits the names into different lines
print "number of names"
num = len(string)  #make num equal to the amount of names
print len(string) #print the number of line so the amount of names
mean = integer / num  #the mean is now the number of integers/ the number of names
print "the mean amount of letters"
print mean


