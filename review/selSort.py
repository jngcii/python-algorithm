def selSort(a):

    for i in range(0, len(a)-1):

        for j in range(i+1, len(a)):

            if a[i] > a[j]:

                a[i], a[j] = a[j], a[i]


arr = [2,4,6,3,5,1,9,7,12]

selSort(arr)

print(arr)