"""
Class test - question 2
c1306213
"""

f = open('classtestdata.csv', 'r')
csvdata = csv.reader(f)
data = [row for row in csvdata]
f.close()
