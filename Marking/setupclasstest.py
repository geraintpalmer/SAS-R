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
#rawdata = [[r.strip() for r in row[:-1]] for row in rawdata if row[-1] != '']
rawdata = [[r.strip() for r in row[:3]] for row in rawdata]
f.close()

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


i = 0
for slot in classtestrooms:
    for e in range(classtestrooms[slot]):
        if len(rawdata) > e + i:
            rawdata[e+i].append(slot)
    i += classtestrooms[slot]

rawdata = sorted(rawdata, key=lambda x : x[0])

busyat1400 = ["CHAMBERS",
              "CHANT",
              "COLE",
              "DAVIES",
              "DAVIES",
              "DAVIS",
              "DIAKUN",
              "DUNKLEY",
              "EARNSHAW",
              "EDWARDS",
              "EWEN",
              "FERRO KIRBY",
              "FORD",
              "FOWLER",
              "FROUDE",
              "GARDNER",
              "GHANAVATI",
              "GIBBS",
              "LOUGHNANE",
              "YIP"]

busyat1500 = ["ADDIS",
              "ALI",
              "AMBLER",
              "ASKILL",
              "AVRAAM",
              "BADCOCK",
              "BAHADORI",
              "BALDWIN",
              "BARR",
              "BATEMAN",
              "BATEMAN",
              "BATHERS",
              "BELL",
              "BORMAN",
              "BROWNHILL",
              "CHEMJONG",
              "FOULKES",
              "JONES",
              "JONES",
              "SMITH",
              "WOODS"]

def findclashes():
    clashes = []
    for row in rawdata:
        if ("1500" in row[-1] and row[1] in busyat1500) or ("1400" in row[-1] and row[1] in busyat1400):
            clashes.append(row)
    return clashes


print "Randomly swapping clashes"
while len(findclashes()) > 0:  # Randomly swap students until we no longer have clashes
    swprow = choice(rawdata)
    clshrow = findclashes()[0]
    swprow[-1], clshrow[-1] = clshrow[-1], swprow[-1]


outfile = open('classtest.csv', 'w')
writeobj = csv.writer(outfile)
for e in rawdata:
    writeobj.writerow(e)
outfile.close()
