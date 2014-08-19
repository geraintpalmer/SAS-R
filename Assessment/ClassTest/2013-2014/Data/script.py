#!/usr/bin/env python

import csv
import random

f = open('namesdatabase.csv','U')
csvrdr = csv.reader(f)
data = [row for row in csvrdr]
f.close()
data = data[1:]

data = random.sample(data,400)

f = open('classtestdata.csv','w')
csvwtr = csv.writer(f)
for k in range(5000):
    csvwtr.writerow(random.choice(data))
f.close()
