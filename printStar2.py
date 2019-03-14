def star(n):

    for i in range(n-1, -1, -1):

        j = 2*n - 2*i - 1

        print(" "*i + "*"*j + " "*i)

star(5)