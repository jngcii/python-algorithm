def recursion(n):

    if n == 0:

        return 0

    return n + recursion(n-1)


print(recursion(100))
