#!/usr/bin/env python

import csv
import argparse
from random import choice

"""
Script return a csv file with students and their schedule
"""

parser = argparse.ArgumentParser(description='Identify schedule for class test')
parser.add_argument('rawdata', help='A data file with 4 columns, number, first name, last name and group')
args = parser.parse_args()
rawdata = args.rawdata

print 'Reading students from %s' % rawdata

f = open(rawdata, 'r')
rawdata = csv.reader(f)
rawdata = [[r.strip() for r in row[:3]] for row in rawdata]
f.close()

class Slot():
    def __init__(self, label, capacity):
        self.label = label
        self.students = []
        self.capacity = capacity
        self.time = label[:4]
        self.room = label[7:]
        self.full = False

class Student():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.scheduled = False
        self.hasclash = False
    def schedule(slot):
        self.slot = slot
        self.slot.students.append(self)
        if self.slot.capacity == len(self.slot.students):
            self.slot.full = True

classtestrooms = {"1500 - M1.03" : 14,
                  "1500 - M1.05" : 26,
                  "1500 - M1.08" : 10,
                  "1500 - M0.33" : 17,
                  "1500 - M0.35" : 16,
                  "1400 - M1.03" : 14,
                  "1400 - M1.05" : 26,
                  "1400 - M1.08" : 10,
                  "1400 - M0.33" : 17,
                  "1400 - M0.35" : 16
                    }

namesbusyat1400 = ["AWAN",
        "BAKER",
        "BIRD",
        "CAMPBELL JAMES",
        "CARNEY",
        "CARPENTER",
        "CHAMBERLAIN",
        "CHAMBERS",
        "CHAN",
        "CHANT",
        "COLE",
        "DAVIES HAYLEY",
        "DAVIES NICK",
        "DAVIS JODIE",
        "DIAKUN",
        "DRENNEN",
        "DUNKLEY",
        "EARNSHAW",
        "EDWARDS",
        "EWEN",
        "FERRO KIRBY",
        "FORD",
        "FOWLER",
        "FOX",
        "FROUDE",
        "FURNELL",
        "GARDNER",
        "GHANAVATI",
        "GIBBS",
        "GRIFFITHS",
        "GRIME",
        "JOHNSON",
        "KATES",
        "LOUGHNANE",
        "MACGINNIS",
        "MAHENDRAN",
        "POHL",
        "SHAH",
        "TATTERSDILL",
        "WELLER",
        "WIGHTMAN",
        "JAC WILLIAMS",
        "YIP"]

namesbusyat1500 = ["ADDIS",
              "ALI",
              "AMBLER",
              "ASKILL",
              "AVRAAM",
              "AYGUN",
              "BADCOCK",
              "BAHADORI",
              "BALDWIN",
              "BARR",
              "BATEMAN",
              "BATEMAN",
              "BATHERS",
              "BELL",
              "BENNETT",
              "BILE",
              "BISWAS",
              "BORMAN",
              "BOWEN GWENNO",
              "BROWNHILL",
              "CHEMJONG",
              "CONWAY",
              "CROFT",
              "DAVIES ELIN",
              "DAVIES MIRIAM",
              "D'SOUZA",
              "FITT",
              "FORMAN",
              "FOULKES",
              "INGRAM",
              "JAMES-OWEN",
              "JONES MARK",
              "JONES NICK",
              "LEWIS",
              "LONG",
              "MAMONA",
              "MARGETTS",
              "MORGAN BEN",
              "PARRY",
              "PATEL",
              "PEACE",
              "ROBERTS",
              "SMITH",
              "STATHAM",
              "THOMAS CORY",
              "THOMAS EMMA",
              "THOMAS RHIA",
              "THOMAS SARA",
              "THOMSON ALEX",
              "THOMSON PIERS",
              "TSANG",
              "WATSON",
              "WHITE ALEXANDRA",
              "GARMON WILLIAMS",
              "WILLSON",
              "WOODS",
              "WYNNE"]

mustbeinroomm016a = ["BAKER",
                     "JENNINGS",
                     "STEFFAN LONG",
                     "MARTIN",
                     "POHL"]

slots = [Slot(e, classtestrooms[e]) for e in classtestrooms]
students = [Student(row[2], row[1]) for row in rawdata]

print [s.fullname for s in students if 'BIRD' in s.fullname]

studentsbusyat1400 = []
studentsbusyat1500 = []
for s in students:
    if any([k in s.fullname for k in namesbusyat1400]):
        studentsbusyat1400.append(s)
    elif any([k in s.fullname for k in namesbusyat1500]):
        studentsbusyat1500.append(s)

print [e for e in namesbusyat1400 if e not in [s.fullname for s in studentsbusyat1400]]

def findclashes():
    clashes = []
    for row in rawdata:
        if ("1500" in row[-1] and any([k in row[2] + " " + row[1]  for k in busyat1500])) or ("1400" in row[-1] and any([k in row[2] + " " + row[1] for k in busyat1400])):
            clashes.append(row)
    return clashes

print "Randomly swapping clashes"
while len(findclashes()) > 0:  # Randomly swap students until we no longer have clashes
    swprow = choice(rawdata)
    clshrow = findclashes()[0]
    swprow[-1], clshrow[-1] = clshrow[-1], swprow[-1]

print "Moving relevant students to M016A"
for row in rawdata:
    for n in mustbeinroomm016a:
        if n in row[2] + " " + row[1]:
            row[-1] = "1400 - M016A"

rawdata = sorted(rawdata, key=lambda x : x[0])
outfile = open('classtest.csv', 'w')
writeobj = csv.writer(outfile)
for e in rawdata:
    writeobj.writerow(e)
outfile.close()
