def mergeRecur(n):

    if(n <= 1):

        return n

    else:

        return n + mergeRecur(n-1)


print(mergeRecur(10))