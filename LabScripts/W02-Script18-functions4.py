def mysum(K=500, B=2):
    s = 0
    k = 0
    while k < K:
        if k % B == 0:
            s += k
        k += 1
    return s

print mysum(50, 13)
print mysum()
print mysum(500, 2)
