def recursion(arr, n):

    if n == 0:

        return arr[n]


    if arr[n] < recursion(arr, n-1):

        return recursion(arr, n-1)

    else:

        return arr[n]



arr1 = [2,6,4,4,2,7,4,8,6,9,4,10,5,3,7]
n = len(arr1)-1
inst1 = recursion(arr1, n)
print(inst1)
