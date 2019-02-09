def merge_sort(a):

    cnt = len(a)

    if cnt <= 1:
        return a

    mid = cnt // 2

    a1 = merge_sort(a[:mid])
    a2 = merge_sort(a[mid:])

    result = []

    while a1 and a2:

        if a1[0] < a2[0]:

            result.append(a1.pop(0))

        else:

            result.append(a2.pop(0))

    while a1:

        result.append(a1.pop(0))

    while a2:

        result.append(a2.pop(0))

    return result


a = [2,6,8,3,5,4,1,9,10]
inst1 = merge_sort(a)
print(inst1)
