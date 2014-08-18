def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)   """ Defining the fibonacci function """

    if n % 2 == 1:      """ if statement to catch case and end function with return """
        return 1
    if n == 0:
        return fib(n-2) + fib(n-1)
    return n == 1

       

