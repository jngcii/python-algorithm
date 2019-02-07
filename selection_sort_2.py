def selection_sort(arr):

    for i in range(0, len(arr)-1):

        for j in range(i+1, len(arr)):

            if arr[i] < arr[j]:

                arr[i], arr[j] = arr[j], arr[i]

    print(arr)


arr = [5,7,1,3,4,8,2,-3,23,99,100,9]
selection_sort(arr)
