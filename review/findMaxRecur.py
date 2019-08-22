def findMaxRecur(arr, n):

    if n <= 1:
        return arr[0]

    max = findMaxRecur(arr,n-1)

    if max > arr[n-1]: return max
    else : return arr[n-1]


arr = [12,42,5,23]

print(findMaxRecur(arr,len(arr)))