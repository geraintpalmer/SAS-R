#!/usr/bin/env python
"""
Script to analyse feedback
"""
import csv
import gspread
import matplotlib.pyplot as plt

class Opinion():
    """
    A class for every opinion
    """
    def __init__(self, label):
        self.label = label
        self.positive = False
        if 'good' in label:
            self.positive = True
        self.mentions = 0

### Download the data from gdrive ###
print "Authenticating"
# Download data
username = "vincent.knight"  # My gmail username
password = "mxsvlamsbbrepuqy"  # App specific password
docid = "0Ah_zrw5uAafbdDVSMGVONTZiRkkwNzJEeDhrMnNVR3c"  # The id for the spreadheet

client = gspread.login(username, password)
spreadsheet = client.open_by_key(docid)  # Create a client object
print "Downloading data"
fulldata = {}  # A dictionary to hold the data by group number
for i, worksheet in enumerate(spreadsheet.worksheets()):
    fulldata[i] = worksheet.get_all_values()  # Read in the data

data = fulldata[0]
####################################

opinions = [Opinion(l) for l in data[0]]  # Create an opinion object for every column of data
for o in opinions:
    o.mentions = len([k[opinions.index(o)] for k in data[1:] if k[opinions.index(o)] != ''])  # Count mentions of opinion

opinions = sorted(opinions, key= lambda x : -x.mentions)

print "================================"
print "Positive comments"
print "================================"
for o in [o for o in opinions if o.positive]:
    print "%s: %s" % (o.label, o.mentions)
print "================================"
print "Negative comments"
print "================================"
for o in [o for o in opinions if not o.positive]:
    print "%s: %s" % (o.label, o.mentions)
