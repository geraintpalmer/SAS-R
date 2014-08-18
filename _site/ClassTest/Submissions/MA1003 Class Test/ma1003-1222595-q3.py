def trapezium(f,n,a,b):
    h=(b-a)/float(n)            #trying to find the area under the graph using the trapezium rule

    area = (0.5)*h
    sum_y = (f(0)+f(b))

    i=a
    while i<b:
        print i                             #summing area of rectangles to get an approximation
        sum_y += 2*f(i)
        i += h

    area *= sum_y


    return area

def f(x):
    return 1 - x ** 2  #funtion



print trapezium(f, 10000, 0, 5)

