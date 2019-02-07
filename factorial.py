def check_sum(n):

    res = 1

    for i in range(1,n+1):

        res = res*i

    return res

inst1 = check_sum(5)
print(inst1)
