def quickSort(arr, left, right):
    
    if right - left <= 0: return

    pivot = arr[right]

    i = left

    for j in range(left, right):

        if arr[j] <= pivot:
        
            arr[i], arr[j] = arr[j], arr[i]

            i += 1
        
    arr[i], arr[right] = arr[right], arr[i]

    quickSort(arr, left, i-1)
    quickSort(arr, i+1, right)


d = [5,2,3,8,9,12,1,7]

quickSort(d, 0, len(d)-1)

print(d)