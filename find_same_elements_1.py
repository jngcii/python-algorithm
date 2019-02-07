def x_func(n):

    res = []

    for i in range(0, len(n)-1):

        for j in range(i+1, len(n)):

            if n[i] == n[j]:

                if n[i] not in res:

                    res.append(n[i])

    return res

arr1 = [1,2,1,4,5,2,3,7,7]
inst1 = x_func(arr1)
print(inst1)
