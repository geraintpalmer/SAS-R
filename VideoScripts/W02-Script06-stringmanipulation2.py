sprinter = "Usain Bolt"
year = 2009
record = 9.58

print int(record)
print float(int(record))

s = str(record)
print type(s)
print s

string = "In " + str(year) + " " + sprinter + " ran the 100 metres in " + str(record) + " seconds."
print string

string = "In %i %s ran the 100 metres in %.02f seconds." % (year, sprinter, record)
print string
