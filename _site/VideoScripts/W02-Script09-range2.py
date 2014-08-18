s = 0
for i in range(2000):
    if i % 3 == 0:
        print "adding %i to s" % i
        s += i
    else:
        print "not adding %i to s" % i
print s
