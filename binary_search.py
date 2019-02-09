def binary_search_sub(a, start, end, n):

    cnt = end - start

    if cnt < 1:

        return start

    m = (cnt + 1) // 2

    mid = start + m


    if n == a[mid]:

        return mid

    elif n < a[mid]:

        return binary_search_sub(a, start, mid - 1, n)

    elif n > a[mid]:

        return binary_search_sub(a, mid + 1, end, n)


def binary_search(a, n):

    return binary_search_sub(a, 0, len(a)-1, n)


a = [1,3,5,7,8,9,10]
inst1 = binary_search(a, 10)
print("it's in {} of {}".format(inst1, len(a)+1))
