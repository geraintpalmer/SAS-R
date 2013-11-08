"""
Class test - question 1
C1332590
"""


def fibonaccirec(n):
    """
    This function will give the nth fibinacci number using a recursive meathod

    Arguments: n, which is an integer

    Outputs: the nth fibonacci number
    """
    if n == 0:  #this is checking the base case n=0
        return 0
    if n == 1:  #this is checking the other base case n=1
        return 1
    return fibonaccirec(n-1) + fibonaccirec(n-2)  #If not the base case, use recursion and the formula for the fibonacci numbers


print "The Fibonacci numbers, for 0 <= n < 11 are..."
for i in range(11):  #as 0 is included, and 11 isnt in this range, it will print n for the given inequalities in the exam question
    print "fibonacci(%s)=%s" % (i, fibonaccirec(i))
