def quick_sort_sub(a, start, end):

    if end - start <= 0:

        return

    pivot = a[end-1]

    i = start

    for j in range(start, end):

        if a[j] <= pivot:

            a[i], a[j] = a[j], a[i]

            i += 1

    quick_sort_sub(a, start, i-2)
    quick_sort_sub(a, i, end)


def quick_sort(a):

    quick_sort_sub(a, 0, len(a))


a = [1,2,3,4,7,8,9,5]
quick_sort(a)

print(a)
