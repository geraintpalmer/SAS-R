#!/usr/bin/env python
"""
Script to download tickable information
"""
import csv
import gspread

username = "vincent.knight"
password = "mxsvlamsbbrepuqy"

docid = "0Ah_zrw5uAafbdEd4M0RiUWFONW1uUHJjU1lmeExKNkE"

client = gspread.login(username, password)
spreadsheet = client.open_by_key(docid)
for i, worksheet in enumerate(spreadsheet.worksheets()):
    filename = docid + '-worksheet' + str(i) + '.csv'
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(worksheet.get_all_values())
