#!/usr/bin/env python
"""
Script to download tickable information
"""
import csv
import gspread
import matplotlib.pyplot as plt

class Student():
    """
    A class for a student
    """
    def __init__(self,name):
        self.name = name
        self.ticks = []

class Group():
    """
    A class for a tutor group
    """
    def __init__(self, number, data):
        self.number = number
        self.students = [Student(name) for name in data[0][1:]]
        self.rawdata = data[1:]
        for row in self.rawdata:
            if 'A' not in row[0]:
                k = 1
                for student in self.students:
                    if row[k] == '':
                        student.ticks.append(False)
                    else:
                        student.ticks.append(True)
                    k += 1
        self.numberofticks = [len([t for t in s.ticks if t]) for s in self.students]



# Download data
username = "vincent.knight"
password = "mxsvlamsbbrepuqy"  # App specific password

docid = "0Ah_zrw5uAafbdEd4M0RiUWFONW1uUHJjU1lmeExKNkE"

client = gspread.login(username, password)
spreadsheet = client.open_by_key(docid)
print "Downloading data"
fulldata = {}
for i, worksheet in enumerate(spreadsheet.worksheets()):
    filename = docid + '-worksheet' + str(i) + '.csv'
    fulldata[i] = worksheet.get_all_values()

print "Collating data"
groups = []  # Create groups (and students)
for i in fulldata:
    groups.append(Group(i, fulldata[i]))

groupnames = {0:"P",
              1:"R",
              2:"S",
              3:"T",
              4:"U",
              5:"V",
              6:"W",
              7:"X",
              8:"Y",
              9:"Z"}

print "Plotting data"
allcounts = []
for g in groups:
    groupname = groupnames[g.number]
    plt.figure()
    plt.hist(g.numberofticks)
    plt.xlabel("Number of ticks")
    plt.ylabel("Proportion")
    plt.title("Group %s" % groupname)
    plt.savefig("%s.pdf" % groupname)
    allcounts += g.numberofticks


plt.figure()
plt.hist(allcounts)
plt.xlabel("Number of ticks")
plt.ylabel("Proportion")
plt.title("All")
plt.savefig("All.pdf")
