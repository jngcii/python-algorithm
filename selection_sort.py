def selection_sort(arr):

    result = []

    for i in range(len(arr)):

        min_idx = 0

        for j in range(1, len(arr)):

            if arr[j] < arr[min_idx]:

                min_idx = j

        result.append(arr[min_idx])
        arr.pop(min_idx)

    print(result)




arr = [5,7,1,3,4,8,2,23,99,100,-2,9]
selection_sort(arr)
