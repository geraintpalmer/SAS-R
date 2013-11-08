textfile = open('classtestdata.txt', 'r') # Opens a file in read mode
string = textfile.read() # Reads the file as a string
print string # Prints the string to screen

data = string.split('\n') # This uses the split method which creates a list from a string
print data
print len(data) - 1 # This will print the length of the list -1

print len(string) - 1

def mydiv(a, b):
    return a / b # Uses the return function which gives a value to the funtion, but doesn't print anything

print mydiv(len(string) - 1, len(data) - 1) # Use to print




