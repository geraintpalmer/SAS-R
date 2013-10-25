#!/usr/bin/env python
"""
Script to download tickable information
"""
import csv
import gspread
import matplotlib.pyplot as plt
from subprocess import call
from os import remove

class Student():
    """
    A class for a student

    Attributes:
        name: A string
        ticks: A list of booleans
    """
    def __init__(self,name):
        """
        Initialises the student

        Arguments: name (a string)
        """
        self.name = name
        self.ticks = []

class Group():
    """
    A class for a tutor group

    Arguments:
        number: integer (corresponding to sheet number on spreadsheet)
        data: a raw data file in the format of the spreadsheets (gspread ensures this will be a list)

    Attributes:
        number: integer (corresponding to sheet number on spreadsheet)
        students:  a list of Student objects
        rawdata: the raw csv file read in as a list
        numberofticks: a list of integers corresponding to the number of ticks of each student
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



print "Authenticating"
# Download data
username = "vincent.knight"  # My gmail username
password = "mxsvlamsbbrepuqy"  # App specific password
docid = "0Ah_zrw5uAafbdEd4M0RiUWFONW1uUHJjU1lmeExKNkE"  # The id for the spreadheet

client = gspread.login(username, password)
spreadsheet = client.open_by_key(docid)  # Create a client object
print "Downloading data"
fulldata = {}  # A dictionary to hold the data by group number
for i, worksheet in enumerate(spreadsheet.worksheets()):
    fulldata[i] = worksheet.get_all_values()  # Read in the data

print "Collating data"
groups = []  # Create groups (and students)
for i in fulldata:
    groups.append(Group(i, fulldata[i]))  # This initialises groups

groupnames = {0:"P",
              1:"R",
              2:"S",
              3:"T",
              4:"U",
              5:"V",
              6:"W",
              7:"X",
              8:"Y",
              9:"Z"}  # For labelling of graphs

print "Plotting data"
allcounts = []
listofpdfs = []
for g in groups:
    groupname = groupnames[g.number]
    plt.figure()
    plt.hist(g.numberofticks)
    plt.xlabel("Number of ticks")
    plt.ylabel("Frequency")
    plt.title("Group %s" % groupname)
    plt.savefig("%s.pdf" % groupname)
    allcounts += g.numberofticks  # Keep track of total ticks
    listofpdfs.append("%s.pdf" % groupname)

# Plot total histogram
plt.figure()
plt.hist(allcounts)
plt.xlabel("Number of ticks")
plt.ylabel("Frequency")
plt.title("All")
plt.savefig("All.pdf")
listofpdfs.append("All.pdf")

call(["pdftk"] + listofpdfs + ["output","plots.pdf"])
for f in listofpdfs:
    remove(f)
