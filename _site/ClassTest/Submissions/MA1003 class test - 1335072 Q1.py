def recX(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
#when n is equal to 0 or 1 then the value is equal to 1 
    for i in range(0,12):
        return recX(n - 1) + recX(n - 1)
#when n is in equal to 1 but below 11 then the function will add the previous
    #two terms together to give the next term
