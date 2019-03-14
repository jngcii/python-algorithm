def star(n):

    for i in range(0, n):

        j = 2*n - 2*i - 1

        print(" "*i + "*"*j + " "*i)

star(5)