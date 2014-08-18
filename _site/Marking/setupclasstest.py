#!/usr/bin/env python

import csv
import argparse
from random import choice

"""
Script return a csv file with students and their schedule
"""

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
              "JAMES-OWEN ELEN",
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
    def __init__(self, firstname, lastname, number):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = lastname + " " + firstname
        self.scheduled = False
        self.hasclash = False
        self.number = number
    def schedule(self, slot):
        self.slot = slot
        self.slot.students.append(self)
        if self.slot.capacity == len(self.slot.students):
            self.slot.scheduled = True

slots = [Slot(e, classtestrooms[e]) for e in classtestrooms]
studentstoslot = [Student(row[2], row[1], row[0]) for row in rawdata]

studentsbusyat1400 = []
studentsbusyat1500 = []
for s in studentstoslot:
    for k in namesbusyat1400:
        if k in s.fullname:
            studentsbusyat1400.append(s)
    for k in namesbusyat1500:
        if k in s.fullname:
            studentsbusyat1500.append(s)

studentsbusyat1400 = list(set(studentsbusyat1400))
studentsbusyat1500 = list(set(studentsbusyat1500))

print any(["BIRD" in k for k in [s.fullname for s in studentsbusyat1400]])

scheduledstudents = []
fullslots = []
while studentsbusyat1400:
    slt = choice([slt for slt in slots if slt.time == '1500'])
    s = studentsbusyat1400.pop()
    s.schedule(slt)
    if slt.full:
        fullslots.append(slt)
        slots.remove(slt)
    scheduledstudents.append(s)
while studentsbusyat1500:
        slt = choice([slt for slt in slots if slt.time == '1400'])
        s = studentsbusyat1500.pop()
        if s.fullname != "CAMPBELL JAMES":
            s.schedule(slt)
            if slt.full:
                fullslots.append(slt)
                slots.remove(slt)
            scheduledstudents.append(s)

for s in studentstoslot:
    if s not in scheduledstudents:
        if s.fullname != "CAMPBELL JAMES":
            slt = choice(slots)
            s.schedule(slt)
            if slt.full:
                fullslots.append(slt)
                slots.remove(slt)
            scheduledstudents.append(s)

print [s.fullname for s in studentsbusyat1400]

m016a1400 = Slot("1400 - M016A", 200)
m016a1500 = Slot("1500 - M016A", 200)
print "Moving relevant students to M016A"
for s in scheduledstudents:
    for n in mustbeinroomm016a:
        if n in s.fullname:
            if any([n in k for k in namesbusyat1400]):
                s.schedule(m016a1500)
            else:
                s.schedule(m016a1400)


outfile = open('classtest.csv', 'w')
writeobj = csv.writer(outfile)
for s in scheduledstudents:
    writeobj.writerow([s.number, s.lastname, s.firstname, s.slot.label])
outfile.close()
