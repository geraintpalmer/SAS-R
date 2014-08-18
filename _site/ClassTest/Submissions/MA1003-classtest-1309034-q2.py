# This is work on sheet 3
textfile = open('excel', 'w')
# First I import the data from excel to python by creating a file for excel
#the how many are there
#mean length of the file


def binarysearch(data, item):
    data.sort()
    first = 0
    last = len(data) - 1
    found = False
    while first <= last and not found:
        middle = int((first + last) / 2)
        if item == data[middle]:
            found = True
        elif item < data[middle]:
            last = middle - 1
        else:
            first = middle + 1
    if data[middle] == item:
        return middle
    return False
alist = [7, 45, 1, 34, 12, 87, 67]
print binarysearch(alist, 33)

def insertionsort(data):
    firstUnsorted = 0
    while firstUnsorted < len(data) - 1:
        indexOfSmallest = firstUnsorted
        index =firstUnsorted + 1
        while index <= len(data) - 1:
            if data(index) < data[indexOfSmallest]:
                indexOfSmallest = index
            index += 1
        data[firstUnsorted], data[indexOfSmallest] = data[indexOfSmallest], data[firstUnsorted]
        firstUnsorted += 1

mylist = []
for i in range(11):
    if i % 2 == 0:
        mylist.append(i)
print mylist


SORT THE LIST (excel):
SET INDEX TO 0
SET FOUND TO short
WHILE INDEX < LENGTH and NOT FOUND:
    IF DATA[INDEX] = ITEM:
        FOUND = TRUE
    ELSE IF DATA[INDEX] > ITEM:
        INDEX = LENGTH
    ELSE:
        INDEX = INDEX + 1
IF FOUND:
    RETURN INDEX
ELSE:
    RETURN "ITEM NOT IN LIST"

    
