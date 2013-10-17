#!/usr/bin/env python

import csv
import argparse

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
rawdata = [[r.strip() for r in row[:-1]] for row in rawdata if row[-1] != '']
f.close()

classtestrooms = {"1300 - M1.03" : 14,
                  "1300 - MSc Computing Lab" : 26,
                  "1300 - MSc Reading Room" : 10,
                  "1300 - M0.33" : 17,
                  "1300 - M0.35" : 16,
                  "1400 - M1.03" : 14,
                  "1400 - MSc Computing Lab" : 26,
                  "1400 - MSc Reading Room" : 10,
                  "1400 - M0.33" : 17,
                  "1400 - M0.35" : 16
                    }

i = 0
for slot in classtestrooms:
    for e in range(classtestrooms[slot]):
        if len(rawdata) > e + i:
            rawdata[e+i].append(slot)
    i += classtestrooms[slot]

rawdata = sorted(rawdata, key=lambda x : x[-1])

outfile = open('classtest.csv', 'w')
writeobj = csv.writer(outfile)
for e in rawdata:
    writeobj.writerow(e)
outfile.close()
