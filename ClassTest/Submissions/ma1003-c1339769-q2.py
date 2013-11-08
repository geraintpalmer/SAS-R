"""
Class test - question 2
c1339769
"""

import csv  # I am importing this library as it can also be used to import data

f = open('classtestdata.csv', 'r')
classtestdata = csv.reader(f)

totalnames = sum(1 for row in classtestdata)  # This adds 1 for each row in the data

print totalnames

def csv_average(filename, row):

    """
    Returns the average of the values in
    column for the csv file
    """

    row_values = []

    with open(filename) as f:
        reader = csv.reader(f)
        for column in reader:
            row_values.append(column[row])

    return sum(row_values) / len(row_values)

print csv_average(classtestdata, 5000)
