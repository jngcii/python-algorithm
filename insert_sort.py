def find_idx(result, value):

    for i in range(0,len(result)):

        if value < result[i]:

            return i

    return len(result)


def insert_sort(arr):

    result = []

    while arr:

        value = arr.pop(0)

        idx = find_idx(result, value)

        result.insert(idx, value)

    print(result)



array = [6,7,2,8,1,4,0]
insert_sort(array)
