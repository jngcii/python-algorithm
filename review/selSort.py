def selSort(a):

    for i in range(0, len(a)-1):

        maxIdx = i

        for j in range(i+1, len(a)):

            if a[maxIdx] > a[j]:

                a[maxIdx], a[j] = a[j], a[maxIdx]


arr = [2,4,6,3,5]

selSort(arr)

print(arr)